-- Table: db_DxCorp.tblTipos_Passo

-- DROP TABLE IF EXISTS "db_DxCorp"."tblTipos_Passo";

CREATE TABLE IF NOT EXISTS "db_DxCorp"."tblTipos_Passo"
(
    id_tipo_passo integer NOT NULL DEFAULT nextval('"db_DxCorp"."tblTipos_Passo_id_tipo_passo_seq"'::regclass),
    ds_tipo_passo character varying(100) COLLATE pg_catalog."default" NOT NULL,
    CONSTRAINT "tblTipos_Passo_pkey" PRIMARY KEY (id_tipo_passo)
)

TABLESPACE pg_default;

ALTER TABLE IF EXISTS "db_DxCorp"."tblTipos_Passo"
    OWNER to "diego.assis";