import json, os
import numpy as np
import scipy.io as sio

# Replace 'your_file.json' with the path to your JSON file
file_path = 'transforms.json'

# Read the JSON file and convert it into a Python object
with open(file_path, 'r') as file:
    data = json.load(file)

# Now 'data' is a Python object containing the data from the JSON file

cam_frames = data['frames'][::-1]
cams = []

def swap_y_z(a):
    t = a[1]
    a[1]=a[2]
    a[2]=t

for frame in cam_frames:
    m = np.array(frame['transform_matrix'])
    center = m[:3, 3]
    swap_y_z(center)

    direction = -m[:3, 2]
    swap_y_z(direction)

    right = m[:3, 0]
    swap_y_z(right)

    up = m[:3, 1]
    swap_y_z(up)
    cams.append(
            {
                'center': center, 
                'direction': direction, 
                'right': right, 
                'up': up, 
            }
        )
sio.savemat(
        os.path.join('cam_data.mat'),
        {'cam': cams})