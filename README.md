# Projeto FastAPI

Este é um projeto construído com FastAPI que fornece uma API RESTful para interagir com um banco de dados PostgreSQL. O FastAPI é um framework moderno e de alto desempenho para construir APIs web com Python.

## Objetivo 
Demonstrar a criação de endpoints RESTful para operações CRUD (Create, Read, Update, Delete) em um banco de dados PostgreSQL, utilizando as capacidades assíncronas do FastAPI e do asyncpg para melhorar o desempenho e a escalabilidade da aplicação.

## Diagrama de Arquitetura

![Diagrama de Arquitetura](Projeto_FastAPI_Postgres.png)

## Estrutura do Projeto

- **Main.py**: Este arquivo contém o código principal da aplicação FastAPI.
- **bd.py**: Arquivo que contém métodos para interagir com o banco de dados PostgreSQL, utilizando a biblioteca `asyncpg` para operações assíncronas.
- **API FastAPI**: Define as rotas da API e a lógica de negócios correspondente, aproveitando as capacidades do framework FastAPI.
- **PostgreSQL**: O banco de dados usado para armazenar os dados da aplicação, com comunicação assíncrona por meio da biblioteca `asyncpg`.
- **Uvicorn**: Servidor ASGI de alto desempenho utilizado para executar a aplicação FastAPI.


## Funcionalidades

Esta API segue o estilo arquitetural REST (Representational State Transfer) e utiliza os métodos HTTP (GET, POST,PATCH e DELETE) para realizar operações CRUD (Create, Read, Update, Delete).

- **Inserção de Tipos de Passos (POST)**: Permite adicionar novos tipos de passos à base de dados.
- **Atualização de Tipos de Passos (PATCH)**: Permite atualizar os tipos de passos existentes com base no ID.
- **Exclusão de Tipos de Passos (DELETE)**: Permite excluir tipos de passos com base no ID.
- **Recuperação de Tipos de Passos (GET)**: Recupera tipos de passos com base no ID ou retorna todos os tipos de passos disponíveis.


## Requisitos

1. **Git instalado na máquina**
   - [Download do Git](https://git-scm.com/downloads)

2. **Python instalado na máquina**
   - [Download do Python](https://www.python.org/downloads/)

3. **PostgreSQL instalado na máquina ou na Nuvem**
   - [Download do Postgres](https://www.postgresql.org/download/)
   - [Postgres na Nuvem - Render](https://render.com/)

## Como Usar

1. **Clone este repositório:**

    ```bash
    git clone https://github.com/Dxis/Projeto_FastAPI_Postgres.git

    ```

2. **Instale as dependências listadas no arquivo `requirements.txt`:**

    ```bash
    pip install fastapi uvicorn python-dotenv asyncpg
    ```

3. **Configure as variáveis de ambiente no arquivo `.env` com as informações do banco de dados PostgreSQL:**

    ```bash
    CONN_POSTGRESQL=postgres://username:password@localhost:5432/database_name
    ```

4. **Inicie o servidor:**

    ```bash
    uvicorn main:app --reload
    ```
6. Você pode acessar a documentação da API em `http://localhost:8000/docs`.

## Contribuição

Contribuições são bem-vindas! Sinta-se à vontade para abrir uma issue ou enviar um pull request.

## Licença

Este projeto é distribuído sob a licença MIT. Consulte o arquivo `LICENSE` para obter mais detalhes.
