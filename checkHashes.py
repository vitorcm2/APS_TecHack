from argparse import ArgumentParser
from components.directoryHash import GetHashofDirs
from components.fileHash import GetFileHash
import json
import requests
from dotenv import load_dotenv
import os

if __name__ == "__main__":
    # parser = ArgumentParser(description=MSG_DESCRIPTION)
    # parser.add_argument(
    #     "file", help="File containing directories and files to be hashed."
    # )

    # args = parser.parse_args()

    load_dotenv(verbose=True)
    token = os.getenv("TOKEN")
    chat_id = os.getenv("CHAT_ID")
    url_base = f"https://api.telegram.org/bot{token}/"

    with open("output.json", "r") as f:
        data = json.load(f)

    error = []

    for i in data:
        try:
            result = GetHashofDirs(i)
        except:
            result = GetFileHash(i)

        if data[i] != result:
            error += [i]

    resp = "Os seguintes arquivos ou diretórios foram modificados:\n\n"

    if len(error) > 0:
        for k, i in enumerate(error):
            resp += f"{k+1}. " + i + "\n"

        link_requisicao = f"{url_base}sendMessage?chat_id={chat_id}&text={resp}"
        requests.get(link_requisicao)
