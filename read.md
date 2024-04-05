# Projeto FastAPI

Este é um projeto construído com FastAPI que fornece uma API RESTful para interagir com um banco de dados PostgreSQL. O FastAPI é um framework moderno e de alto desempenho para construir APIs web com Python.

## Objetivo 
Demonstrar a criação de endpoints RESTful para operações CRUD (Create, Read, Update, Delete) em um banco de dados PostgreSQL, utilizando as capacidades assíncronas do FastAPI e do asyncpg para melhorar o desempenho e a escalabilidade da aplicação.

## Diagrama de Arquitetura

![Diagrama de Arquitetura](Projeto_FastAPI_Postgres.png)

## Estrutura do Projeto

- **Main.py**: Este arquivo contém o código principal da aplicação FastAPI.
- **bd.py**: Arquivo que contém métodos para interagir com o banco de dados PostgreSQL.
- **API FastAPI**: Define as rotas da API e a lógica de negócios correspondente.
- **PostgreSQL**: O banco de dados usado para armazenar os dados da aplicação.

## Funcionalidades

- **Inserção de Tipos de Passos**: A API permite inserir novos tipos de passos.
- **Atualização de Tipos de Passos**: Possibilidade de atualizar os tipos de passos existentes.
- **Exclusão de Tipos de Passos**: Permite excluir tipos de passos com base no ID.
- **Recuperação de Tipos de Passos**: Recupera tipos de passos com base no ID ou retorna todos os tipos de passos.

## Como Usar

1. **Clone este repositório:**

    ```bash
    git clone https://github.com/seu-usuario/nome-do-repositorio.git
    ```

2. **Instale as dependências listadas no arquivo `requirements.txt`:**

    ```bash
    pip install -r requirements.txt
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
