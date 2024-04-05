from fastapi import FastAPI

# Criar uma instância do FastAPI
app = FastAPI()

#arquivo json teste
vendas = {
    1: {"Produto":"teste","Descricao":"teste","Preco":1},
    2: {"Produto":"teste2","Descricao":"teste","Preco":1,"Imagem":"Caminho"},
    3: {"Produto":"teste2","Descricao":"teste","Preco":1,"UF":"SP"}          
}

# Rota padrão
@app.get("/")
def home():
    return {"message": "Olá, FastAPI"}

# Rota com parâmetros
@app.get("/vendas/{item_id}")
def RetornaVenda(item_id: int):
    if item_id in vendas:
        return vendas[item_id]
    else:
        return {"Obs":"Venda não encontrada"}
    
    
#arquivo json teste
Cadastro_Tarefas = {
    1: {"tarefa 1":"proc 1","Descricao":"teste","schema":1},
    2: {"tarefa 2":"proc 1","Descricao":"teste","schema":1},
    3: {"tarefa 3":"Captura de arq","Descricao":"teste","schema":1,"Caminho":"Caminho"}          
}

# Rota teste parâmetros
@app.get("/Cadastro_Tarefas/{item_id}")
def RetornaVenda(item_id: int):
    if item_id in Cadastro_Tarefas:
        return Cadastro_Tarefas[item_id]
    else:
        return {"Obs":"Venda não encontrada"}
