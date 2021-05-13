from argparse import ArgumentParser
from components.directoryHash import GetHashofDirs
from components.fileHash import GetFileHash
import json

if __name__ == "__main__":
    # parser = ArgumentParser(description=MSG_DESCRIPTION)
    # parser.add_argument(
    #     "file", help="File containing directories and files to be hashed."
    # )

    # args = parser.parse_args()

    with open("output.json", "r") as f:
        data = json.load(f)

    status = True

    for i in data:
        try:
            result = GetHashofDirs(i)
        except:
            result = GetFileHash(i)

        if data[i] != result:
            status = False
            print(f"Diferente {i}")
        else:
            status = False
            print(f"Passou {i}")