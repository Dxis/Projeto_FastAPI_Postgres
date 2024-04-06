-- Table: db_DxCorp.tblTipos_Passo

-- DROP TABLE IF EXISTS "db_DxCorp"."tblTipos_Passo";

CREATE TABLE IF NOT EXISTS "db_DxCorp"."tblTipos_Passo" (
    id_tipo_passo SERIAL PRIMARY KEY,
    ds_tipo_passo VARCHAR(100) NOT NULL
);


