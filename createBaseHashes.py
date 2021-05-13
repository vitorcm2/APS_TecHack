from argparse import ArgumentParser
from components.directoryHash import GetHashofDirs
from components.fileHash import GetFileHash
import json


MSG_DESCRIPTION = "Create Base hashes of directories and files."


if __name__ == "__main__":
    parser = ArgumentParser(description=MSG_DESCRIPTION)
    parser.add_argument(
        "file", help="File containing directories and files to be hashed."
    )

    args = parser.parse_args()

    with open(args.file, "r") as f:
        data = f.read()

    data = data.strip().split()

    result = {}

    for i in data:
        try:
            result[i] = GetHashofDirs(i)
        except:
            result[i] = GetFileHash(i)

    with open("output.json", "w") as f:
        json.dump(result, f, indent=4)
