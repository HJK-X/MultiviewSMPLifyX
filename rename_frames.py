import os
import math

def renm(fp, pr):
    files = os.listdir(fp)
    print(os.getcwd())

    td = math.ceil(math.log10(len(files)+1)) if len(files)>0 else 1

    for ind, file in enumerate(files):
        fxt = os.path.splitext(file)[1]
        i = str(ind).zfill(td)
        nf = f"{i}{pr}{fxt}"

        cp = os.path.join(fp, file)
        np = os.path.join(fp, nf)

        os.rename(cp, np)

renm('./', '_keypoints')