import asyncpg
import asyncio
import os
from dotenv import load_dotenv
# Importe o módulo json
import json

# Carrega as variáveis de ambiente do arquivo .env
load_dotenv()

# Obtém a string de conexão do banco de dados do arquivo .env
CONN_POSTGRESQL = os.getenv("CONN_POSTGRESQL")

# Função para conectar ao banco de dados
async def connect_to_db():
    return await asyncpg.connect(CONN_POSTGRESQL)

# Métodos CRUD para a tabela tblTarefas

# Método para obter os tipos de passos da tabela tblTipos_Passo
async def get_tipo_passo_by_id(tipo_passo_id):
    con = await asyncpg.connect(CONN_POSTGRESQL)
    if tipo_passo_id is not None:
        query = await con.fetch('SELECT * FROM "db_DxCorp"."tblTipos_Passo" WHERE ID_Tipo_Passo = $1', tipo_passo_id)
        #print((query))
    else:
        query = await con.fetch('SELECT * FROM "db_DxCorp".SPR_SEL_TIPOS_PASSOS(2);')
        #print((query))        
   
    return(query)

# Método para obter os tipos de passos da tabela tblTipos_Passo
async def get_tipos_passos():
    con = await asyncpg.connect(CONN_POSTGRESQL)
    query = await con.fetch('SELECT * FROM "db_DxCorp"."tblTipos_Passo"')
    return(query)

# Método para inserir um novo tipo de passo na tabela tblTipos_Passo
async def spr_ins_tipos_passo(ds_tipo_passo):
    try:
        con = await connect_to_db()
        await con.execute('''
            INSERT INTO "db_DxCorp"."tblTipos_Passo" (ds_Tipo_Passo)
            VALUES ($1)
        ''', ds_tipo_passo)
        return {"success": True, "message": "Tipo de passo inserido com sucesso"}
    except Exception as e:
        return {"success": False, "message": f"Erro ao inserir tipo de passo: {str(e)}"}

#delete tipo passo
async def spr_del_tipo_passo(id_tipo_passo):
    try:
        con = await connect_to_db()
        await con.execute('CALL "db_DxCorp".spr_del_tipos_passos($1)', id_tipo_passo)
        return {"success": True, "message": "Tipo de passo excluído com sucesso"}
    except Exception as e:
        return {"success": False, "message": f"Erro ao excluir tipo de passo: {str(e)}"}


#update tipo passo
async def spr_upd_tipos_passo(id_tipo_passo, ds_tipo_passo):
    try:
        con = await connect_to_db()
        await con.execute('Call "db_DxCorp".spr_upd_tipos_passos($1, $2)',id_tipo_passo, ds_tipo_passo)
        return {"success": True, "message": "Tipo passo atualizado"}  
    except Exception as e:
        return {"success": False, "message": f"Erro ao excluir tipo de passo: {str(e)}"}





"""
# Método teste
async def run(tipo_passo_id : int):
    con = await asyncpg.connect(CONN_POSTGRESQL)
    query = await con.fetch('SELECT * FROM "db_DxCorp"."tblTipos_Passo" WHERE ID_Tipo_Passo = $1', tipo_passo_id)
    #query = await con.fetch('SELECT * FROM "db_DxCorp"."tblTipos_Passo"')
    ##print(types)
    print((query))

# Executar o código dentro de um loop de evento asyncio
asyncio.get_event_loop().run_until_complete(run(1))
"""