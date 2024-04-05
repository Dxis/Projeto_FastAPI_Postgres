
CREATE OR REPLACE PROCEDURE "db_DxCorp".spr_upd_tipos_passos(
    IN id_tipo_passo_param integer,
    IN novo_ds_tipo_passo_param character varying
)
LANGUAGE 'plpgsql'
AS $$
BEGIN
    UPDATE "db_DxCorp"."tblTipos_Passo"
    SET Ds_Tipo_Passo = novo_ds_tipo_passo_param
    WHERE ID_Tipo_Passo = id_tipo_passo_param;
END;
$$;
