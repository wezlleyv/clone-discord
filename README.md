<h1 align="center"><img width=400 height=200 src="./static/images/Discord-logo.png"></h1>

<h1 align="center">Discord clone</h1>

## Overview
Este projeto visa criar um clone da popular plataforma de comunicação Discord usando Python e o framework de desenvolvimento web Django. O objetivo é replicar alguns dos principais recursos e funcionalidades do Discord, como mensagens em tempo real e gerenciamento de servidor. O projeto utilizará os recursos de back-end do Django para lidar com a autenticação do usuário, armazenamento de dados. Além disso, para produção utilizará o servidor web Nginx para gerenciar conexões simultâneas e Docker para automação.
## Instalação
Clone o repositorio no seu diretorio
```sh
cd clone-discord
```
Crie um ambiente virtual e instale as dependências
```sh
python -m venv venv
source ./venv/bin/activate
pip install -r requirements.txt
```
Execute o servidor
```
python manage.py runserver
```
## Instalação com docker
Valido somente na distribuição Arch Linux
Instale o Docker e o Docker-compose
```sh
sudo pacman -Syu
sudo pacman -S docker docker-compose
```
Incie o serviço Docker
```sh
sudo systemctl start docker.service
```

Inicie usando docker compose
```sh
docker compose up --build
```
OBS: Certifique que o Redis.service e 127.0.0.1 estejam livres
```sh
systemctl stop redis.service
```
