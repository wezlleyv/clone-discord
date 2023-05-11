<div align="center"><img width=400 height=200 src="./static/images/Discord-logo.png"></div>

<h1 align="center">Discord clone</h1>

<div align="center">
  <img src="https://img.shields.io/badge/Made%20with-Python-blue">
  <img src="https://img.shields.io/badge/Django-4.2-blue">
  <img src="https://img.shields.io/badge/lincense-MIT-blue">
</div>


Tabela de conteúdos
=================
<!--ts-->
   * [Sobre](#Sobre)
   * [Tabela de Conteudo](#tabela-de-conteudo)
   * [Instalação](#Instalacao)
      * [Instalação docker Arch](#Instalação-com-docker-no-Arch)
   * [Tecnologias](#tecnologias)
<!--te-->


## Sobre
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
## Instalação com docker no Arch
Valido somente na distribuição Arch Linux
<p>Instale o Docker e o Docker-compose</p>
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
