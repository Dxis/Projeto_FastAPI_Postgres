SELECT "db_DxCorp".spr_sel_tipos_passos(null)

INSERT INTO "db_DxCorp"."tblTipos_Passo"( ds_tipo_passo)	VALUES ( 'teste3');



CALL "db_DxCorp".spr_del_tipos_passos(6 );

CALL "db_DxCorp".spr_upd_tipos_passos(7, 'Tipo de Passo Modificado');
