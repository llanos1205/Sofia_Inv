from django.db import models
from Sofia_Server.Sofia_App.Modulos.InfoUser.models import Area,Empresa,Gerencia,Regional,Ubicacion,Cargo,Permiso

class Cuenta(models.Model):
    idcuenta = models.AutoField(db_column='idCuenta', primary_key=True)  # Field name made lowercase.
    usuario = models.CharField(db_column='Usuario', max_length=45, blank=True, null=True)  # Field name made lowercase.
    contrasena = models.CharField(db_column='Contrasena', max_length=45, blank=True, null=True)  # Field name made lowercase.
    estado = models.IntegerField(db_column='Estado')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'cuenta'
    def __str__(self):
        return '%d: %s' % (self.idcuenta, self.usuario)
class UsuarioAd(models.Model):
    idusuario_ad = models.AutoField(db_column='idUsuario_AD', primary_key=True)  # Field name made lowercase.
    nombre = models.CharField(db_column='Nombre', max_length=100, blank=True, null=True)  # Field name made lowercase.
    apellido = models.CharField(db_column='Apellido', max_length=100, blank=True, null=True)  # Field name made lowercase.
    ci = models.CharField(db_column='Ci', max_length=45)  # Field name made lowercase.
    area_idarea = models.ForeignKey(Area, models.SET_NULL, db_column='Area_idArea',null=True)  # Field name made lowercase.
    empresa_idempresa = models.ForeignKey(Empresa, models.SET_NULL, db_column='Empresa_idEmpresa',null=True)  # Field name made lowercase.
    gerencia_idgerencia = models.ForeignKey(Gerencia, models.SET_NULL, db_column='Gerencia_idGerencia',null=True)  # Field name made lowercase.
    regional_idregional = models.ForeignKey(Regional, models.SET_NULL, db_column='Regional_idRegional',null=True)  # Field name made lowercase.
    ubicacion_idubicacion = models.ForeignKey(Ubicacion, models.SET_NULL, db_column='Ubicacion_idUbicacion',null=True)  # Field name made lowercase.
    cuenta_idcuenta = models.ForeignKey(Cuenta, models.SET_NULL, db_column='Cuenta_idCuenta',null=True,related_name="Usuarios")  # Field name made lowercase.
    cargo_idcargo = models.ForeignKey(Cargo, models.SET_NULL, db_column='Cargo_idCargo',null=True)  # Field name made lowercase.
    estado = models.IntegerField(db_column='Estado')  # Field name made lowercase.
    permisos=models.ManyToManyField(Permiso,related_name='Permisos',through='UsuarioAdHasPermiso')
    class Meta:
        managed = False
        db_table = 'usuario_ad'
    def __str__(self):
        return '%d: %s' % (self.idusuario_ad, (self.nombre +"   "+ self.apellido))
class UsuarioAdHasPermiso(models.Model):
    usuario_ad_idusuario_ad = models.ForeignKey(UsuarioAd, models.DO_NOTHING, db_column='Usuario_AD_idUsuario_AD',primary_key=True)  # Field name made lowercase.
    permiso_idpermiso = models.ForeignKey(Permiso, models.DO_NOTHING, db_column='Permiso_idPermiso')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'usuario_ad_has_permiso'
        unique_together = (('usuario_ad_idusuario_ad', 'permiso_idpermiso'))
class UsuarioCorreo(models.Model):
    idusuario_correo = models.AutoField(db_column='idUsuario_Correo', primary_key=True)  # Field name made lowercase.
    correo = models.EmailField(db_column='Correo', max_length=45, blank=True, null=True)  # Field name made lowercase.
    contrasena = models.CharField(db_column='Contrasena', max_length=45, blank=True, null=True)  # Field name made lowercase.
    tipo = models.CharField(db_column='Tipo', max_length=45, blank=True, null=True)  # Field name made lowercase.
    usuario_ad_idusuario_ad1 = models.ForeignKey(UsuarioAd, models.SET_NULL, db_column='Usuario_AD_idUsuario_AD1',null=True)  # Field name made lowercase.
    estado = models.IntegerField(db_column='Estado')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'usuario_correo'
    def __str__(self):
        return '%d: %s' % (self.idusuario_correo, self.correo)
