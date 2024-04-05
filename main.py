from fastapi import FastAPI, HTTPException
from Model import bd
from typing import Optional
from fastapi.staticfiles import StaticFiles

# Criar uma instância do FastAPI
app = FastAPI()

# Rota padrão
@app.get("/")
def home():
    return {"message": "Olá, FastAPI"}


#update tipo passo
@app.patch("/TiposPassos/")
async def spr_upt_tipo_passo(id_tipo_passo: int, ds_tipo_passo: str):
    result = await bd.spr_upd_tipos_passo(id_tipo_passo, ds_tipo_passo)
    if result["success"]:  # Corrigido para usar a chave "success" em vez de "sucess"
        return result["message"]
    else:
        raise HTTPException(status_code=500, detail=result["message"])


#Delete novo passo
@app.delete("/TiposPassos/")
async def spr_del_tipo_passo(id_tipo_passo: int):
    result = await bd.spr_del_tipo_passo(id_tipo_passo)
    if result["success"]:
        #return {"message": "Tipo de passo criado com sucesso"}
        return result["message"]
    else:
        raise HTTPException(status_code=500, detail=result["message"])

#Insert novo passo
@app.post("/TiposPassos/")
async def insert_tipo_passo(ds_tipo_passo: str):
    result = await bd.spr_ins_tipos_passo(ds_tipo_passo)
    if result["success"]:
        #return {"message": "Tipo de passo criado com sucesso"}
        return result["message"]
    else:
        raise HTTPException(status_code=500, detail=result["message"])

# Rota para obter tarefa por ID
@app.get("/TiposPassos/{tipo_passo_id}")
async def  get_tipo_passo_by_id(tipo_passo_id : Optional[int] = None):
    tipo_passo = await bd.get_tipo_passo_by_id(tipo_passo_id)
    if tipo_passo:
        return dict(tipo_passo)
    else:
        return {"Obs": "Tipo passo não encontrada"}

# Rota para obter tarefa por ID
@app.get("/TiposPassos/")
async def  get_tipos_passos():
    tipo_passo = await bd.get_tipos_passos()
    if tipo_passo:
        return dict(tipo_passo)
    else:
        return {"Obs": "Tipo passo não encontrada"}