from components.directoryHash import GetHashofDirs
from components.fileHash import GetFileHash
import json
import os


MSG_DESCRIPTION = "Create Base hashes of directories and files."

def getdirfiles(path):
    listdir = os.listdir(path)
    data = []

    for i in listdir:
        if not(os.path.isdir(path+i)):
            data += [path+i]
        else:
            data += [path+i+"/"]
            data += getdirfiles(path+i+"/")

    return data


if __name__ == "__main__":
    
    basedir = "./test/"
    
    data = getdirfiles(basedir)

    result = {}

    for i in data:
        try:
            result[i] = GetHashofDirs(i)
        except:
            result[i] = GetFileHash(i)

    with open("output.json", "w") as f:
        json.dump(result, f, indent=4)
