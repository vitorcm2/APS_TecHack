import hashlib


def GetFileHash(file):
    md5_hash = hashlib.md5()

    a_file = open(file, "rb")
    content = a_file.read()
    md5_hash.update(content)

    digest = md5_hash.hexdigest()
    return digest
