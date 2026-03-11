🚀 Script Plennus - Instalação Rápida

Este projeto automatiza a geração de planilhas de atividades baseadas no histórico de commits do Git.
1. Pré-requisitos (Sistema)

No Ubuntu 24.04, instale as dependências básicas:
Bash

sudo apt update && sudo apt install python3-pip python3-venv curl git -y

2. Instalar o Poetry

Instale o gerenciador de pacotes (se ainda não tiver):
Bash

curl -sSL https://install.python-poetry.org | python3 -
export PATH="$HOME/.local/bin:$PATH"

3. Configurar o Projeto

Dentro da pasta ~/Ensino/script-plennus, execute:
Bash

# Dar permissão ao script bash
chmod +x plennus

# Configurar o ambiente do Poetry
poetry config virtualenvs.in-project true
poetry install

4. Uso

Sempre que precisar rodar o script:
Bash

poetry run python plennus.py

***************************
No arquivo plennus mudar a url no # informe abaixo o caminho do projeto
export caminho_projetos='~/Ensino/' para pasta raiz de onde ficarão os projetos.

No main do arquivo plennus adicionar novas urls de novos projetos caso houver.