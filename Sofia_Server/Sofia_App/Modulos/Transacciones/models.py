
from django.db import models
class Asociacion(models.Model):
    idasociacion = models.AutoField(db_column='idAsociacion', primary_key=True)  # Field name made lowercase.
    fecha_alta = models.DateField(db_column='Fecha_Alta', blank=True, null=True)  # Field name made lowercase.
    fecha_baja = models.DateField(db_column='Fecha_Baja', blank=True, null=True)  # Field name made lowercase.
    motivo = models.CharField(db_column='Motivo', max_length=75, blank=True, null=True)  # Field name made lowercase.
    equipo_idequipo = models.ForeignKey('Equipo', models.SET_NULL,db_column='Equipo_idEquipo',null=True)  # Field name made lowercase.
    usuariofinal = models.ForeignKey('UsuarioAd', models.SET_NULL,related_name='final', db_column='UsuarioFInal',null=True)  # Field name made lowercase.
    resposable=models.IntegerField(db_column='EsResponsable', blank=True, null=True)
    cuenta_idcuenta=models.ForeignKey('Cuenta', models.SET_NULL,related_name='cuenta', db_column='Cuenta_idCuenta',null=True)
    class Meta:
        managed = False
        db_table = 'asociacion'  
class Auditoria(models.Model):
    idauditoria = models.AutoField(db_column='idAuditoria', primary_key=True)  # Field name made lowercase.
    id_registro_afectado = models.IntegerField(db_column='Id_Registro_Afectado', blank=True, null=True)  # Field name made lowercase.
    tabla_afectada = models.CharField(db_column='Tabla_Afectada', max_length=45, blank=True, null=True)  # Field name made lowercase.
    accion = models.CharField(db_column='Accion', max_length=45, blank=True, null=True)  # Field name made lowercase.
    fecha = models.DateField(db_column='Fecha', blank=True, null=True)  # Field name made lowercase.
    ip = models.CharField(db_column='Ip', max_length=18, blank=True, null=True)  # Field name made lowercase.
    usuario_ad_idusuario_ad = models.ForeignKey('UsuarioAd', models.SET_NULL, db_column='Usuario_AD_idUsuario_AD',null=True)  # Field name made lowercase.
    class Meta:
        managed = False
        db_table = 'auditoria'



