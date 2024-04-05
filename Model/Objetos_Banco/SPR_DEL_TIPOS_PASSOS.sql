CREATE OR REPLACE FUNCTION "db_DxCorp".spr_del_tipos_passos(
    id_tipo_passo_param INT DEFAULT NULL,
    ds_tipo_passo_param VARCHAR(100) DEFAULT NULL
)
RETURNS void 
LANGUAGE plpgsql
AS $$
BEGIN
    IF id_tipo_passo_param IS NOT NULL THEN
        DELETE FROM "db_DxCorp"."tblTipos_Passo"
        WHERE ID_Tipo_Passo = id_tipo_passo_param;
    ELSIF ds_tipo_passo_param IS NOT NULL THEN
        DELETE FROM "db_DxCorp"."tblTipos_Passo"
        WHERE Ds_Tipo_Passo = ds_tipo_passo_param;
    ELSE
        RAISE EXCEPTION 'É necessário fornecer um ID ou uma descrição para exclusão.';
    END IF;
END;
$$;
