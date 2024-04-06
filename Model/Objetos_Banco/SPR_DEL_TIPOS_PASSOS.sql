CREATE OR REPLACE PROCEDURE "db_DxCorp".spr_del_tipos_passos(
	IN id_tipo_passo_param integer 
	)
LANGUAGE 'plpgsql'
AS $BODY$
BEGIN
    IF id_tipo_passo_param IS NOT NULL THEN
        DELETE FROM "db_DxCorp"."tblTipos_Passo"
        WHERE ID_Tipo_Passo = id_tipo_passo_param;
    ELSE
        RAISE EXCEPTION 'Nenhum parâmetro fornecido para exclusão.';
    END IF;
END;
$BODY$;

