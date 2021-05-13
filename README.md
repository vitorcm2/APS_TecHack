# APS TecHack

Na máquina onde queremos verificar os hashes:

Instalação requisitos
> pip install -r requirements.txt

Edite o arquivo `to_check.txt`, passando os diretórios ou arquivos a serem validados.

> nano APS_TecHack/to_check.txt

Rode `createBaseHashes.py` para gerar o hash do arquivo ou diretório.

> python3 APS_TecHack/createBaseHashes.py APS_TecHack/to_check.txt

Crie dentro do diretório clonado um arquivo `.env`, seguindo o template existente para receber notificações por meio do Telegram.

Rode `./APS_TecHack/setup.sh`.

> ./setup.sh

    Obs: caso dê erro de permissão: chmod +x APS_TecHack/setup.sh

