from checksumdir import dirhash


def GetHashofDirs(directory):
    return dirhash(directory)