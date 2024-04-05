-- FUNCTION: db_DxCorp.spr_sel_tipos_passos(integer)

--DROP FUNCTION IF EXISTS "db_DxCorp".spr_sel_tipos_passos(integer);

CREATE OR REPLACE FUNCTION "db_DxCorp".spr_sel_tipos_passos(id_tipo_passo_param integer DEFAULT NULL::integer)

    RETURNS TABLE(id_tipo_passo_ret integer, ds_tipo_passo_ret character varying) 
    LANGUAGE 'plpgsql'
    COST 100
    VOLATILE PARALLEL UNSAFE
    ROWS 1000

AS $BODY$

BEGIN
    IF id_tipo_passo_param IS NOT NULL THEN
        RETURN QUERY SELECT ID_Tipo_Passo, Ds_Tipo_Passo
                     FROM "db_DxCorp"."tblTipos_Passo"
                     WHERE ID_Tipo_Passo = id_tipo_passo_param;
    ELSE
        RETURN QUERY SELECT ID_Tipo_Passo, Ds_Tipo_Passo
                     FROM "db_DxCorp"."tblTipos_Passo";
    END IF;
END;
$BODY$;

ALTER FUNCTION "db_DxCorp".spr_sel_tipos_passos(integer)
    OWNER TO "diego.assis";
