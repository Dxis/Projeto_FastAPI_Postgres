# Projeto FastAPI

Este é um projeto construído com FastAPI que fornece uma API para interagir com um banco de dados PostgreSQL.

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

1. Clone este repositório em sua máquina local.
2. Certifique-se de ter o Python e o PostgreSQL instalados em sua máquina.
3. Instale as dependências do projeto executando `pip install -r requirements.txt`.
4. Configure as variáveis de ambiente necessárias no arquivo `.env`.
5. Execute o arquivo `main.py` para iniciar o servidor FastAPI.
6. Você pode acessar a documentação da API em `http://localhost:8000/docs`.

## Contribuição

Contribuições são bem-vindas! Sinta-se à vontade para abrir uma issue ou enviar um pull request.

## Licença

Este projeto é distribuído sob a licença MIT. Consulte o arquivo `LICENSE` para obter mais detalhes.
