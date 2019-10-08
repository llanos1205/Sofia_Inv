# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Area(models.Model):
    idarea = models.AutoField(db_column='idArea', primary_key=True)  # Field name made lowercase.
    nombre = models.CharField(db_column='Nombre', max_length=45, blank=True, null=True)  # Field name made lowercase.
    descripcion = models.CharField(db_column='Descripcion', max_length=100, blank=True, null=True)  # Field name made lowercase.
    departamento_iddepartamento = models.ForeignKey('Departamento', models.DO_NOTHING, db_column='Departamento_idDepartamento')  # Field name made lowercase.
    estado = models.IntegerField(db_column='Estado')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'area'


class Asociacion(models.Model):
    idasociacion = models.IntegerField(db_column='idAsociacion', primary_key=True)  # Field name made lowercase.
    fecha_alta = models.DateTimeField(db_column='Fecha_Alta', blank=True, null=True)  # Field name made lowercase.
    fecha_baja = models.DateTimeField(db_column='Fecha_Baja', blank=True, null=True)  # Field name made lowercase.
    motivo = models.CharField(db_column='Motivo', max_length=75, blank=True, null=True)  # Field name made lowercase.
    equipo_idequipo = models.ForeignKey('Equipo', models.DO_NOTHING, db_column='Equipo_idEquipo')  # Field name made lowercase.
    usuarioinicial = models.ForeignKey('UsuarioAd', models.DO_NOTHING, db_column='UsuarioInicial', blank=True, null=True)  # Field name made lowercase.
    usuariofinal = models.ForeignKey('UsuarioAd', models.DO_NOTHING, db_column='UsuarioFInal', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'asociacion'


class Atributo(models.Model):
    idatributo = models.AutoField(db_column='idAtributo', primary_key=True)  # Field name made lowercase.
    nombre = models.CharField(db_column='Nombre', max_length=45, blank=True, null=True)  # Field name made lowercase.
    estado = models.IntegerField(db_column='Estado')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'atributo'


class Auditoria(models.Model):
    idauditoria = models.AutoField(db_column='idAuditoria', primary_key=True)  # Field name made lowercase.
    id_registro_afectado = models.IntegerField(db_column='Id_Registro_Afectado', blank=True, null=True)  # Field name made lowercase.
    tabla_afectada = models.CharField(db_column='Tabla_Afectada', max_length=45, blank=True, null=True)  # Field name made lowercase.
    accion = models.CharField(db_column='Accion', max_length=45, blank=True, null=True)  # Field name made lowercase.
    fecha = models.DateTimeField(db_column='Fecha', blank=True, null=True)  # Field name made lowercase.
    ip = models.CharField(db_column='Ip', max_length=18, blank=True, null=True)  # Field name made lowercase.
    usuario_ad_idusuario_ad = models.ForeignKey('UsuarioAd', models.DO_NOTHING, db_column='Usuario_AD_idUsuario_AD')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'auditoria'


class Cargo(models.Model):
    idcargo = models.AutoField(db_column='idCargo', primary_key=True)  # Field name made lowercase.
    nombre = models.CharField(db_column='Nombre', max_length=45, blank=True, null=True)  # Field name made lowercase.
    descripcion = models.CharField(db_column='Descripcion', max_length=100, blank=True, null=True)  # Field name made lowercase.
    estado = models.IntegerField(db_column='Estado')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'cargo'


class Cuenta(models.Model):
    idcuenta = models.AutoField(db_column='idCuenta', primary_key=True)  # Field name made lowercase.
    usuario = models.CharField(db_column='Usuario', max_length=45, blank=True, null=True)  # Field name made lowercase.
    contrasena = models.CharField(db_column='Contrasena', max_length=45, blank=True, null=True)  # Field name made lowercase.
    estado = models.IntegerField(db_column='Estado')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'cuenta'


class Departamento(models.Model):
    iddepartamento = models.AutoField(db_column='idDepartamento', primary_key=True)  # Field name made lowercase.
    nombre = models.CharField(db_column='Nombre', max_length=45, blank=True, null=True)  # Field name made lowercase.
    descripcion = models.CharField(db_column='Descripcion', max_length=100, blank=True, null=True)  # Field name made lowercase.
    estado = models.IntegerField(db_column='Estado')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'departamento'


class Empresa(models.Model):
    idempresa = models.AutoField(db_column='idEmpresa', primary_key=True)  # Field name made lowercase.
    nombre = models.CharField(db_column='Nombre', max_length=45, blank=True, null=True)  # Field name made lowercase.
    descripcion = models.CharField(db_column='Descripcion', max_length=100, blank=True, null=True)  # Field name made lowercase.
    estado = models.IntegerField(db_column='Estado')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'empresa'


class Equipo(models.Model):
    idequipo = models.AutoField(db_column='idEquipo', primary_key=True)  # Field name made lowercase.
    marca = models.CharField(db_column='Marca', max_length=100, blank=True, null=True)  # Field name made lowercase.
    modelo = models.CharField(db_column='Modelo', max_length=100, blank=True, null=True)  # Field name made lowercase.
    nro_serie = models.CharField(db_column='Nro_Serie', max_length=100, blank=True, null=True)  # Field name made lowercase.
    nro_activo_fijo = models.CharField(db_column='Nro_Activo_Fijo', max_length=100, blank=True, null=True)  # Field name made lowercase.
    ip = models.CharField(db_column='Ip', max_length=50, blank=True, null=True)  # Field name made lowercase.
    ultima_observacion = models.CharField(db_column='Ultima_Observacion', max_length=200, blank=True, null=True)  # Field name made lowercase.
    usuario_ad_idusuario_ad = models.ForeignKey('UsuarioAd', models.DO_NOTHING, db_column='Usuario_AD_idUsuario_AD', blank=True, null=True)  # Field name made lowercase.
    estado = models.IntegerField(db_column='Estado')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'equipo'


class Gerencia(models.Model):
    idgerencia = models.AutoField(db_column='idGerencia', primary_key=True)  # Field name made lowercase.
    nombre = models.CharField(db_column='Nombre', max_length=45, blank=True, null=True)  # Field name made lowercase.
    descripcion = models.CharField(db_column='Descripcion', max_length=100, blank=True, null=True)  # Field name made lowercase.
    estado = models.IntegerField(db_column='Estado')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'gerencia'


class Impresora(models.Model):
    idimpresora = models.ForeignKey(Equipo, models.DO_NOTHING, db_column='idImpresora', primary_key=True)  # Field name made lowercase.
    tipo = models.CharField(db_column='Tipo', max_length=45, blank=True, null=True)  # Field name made lowercase.
    tinta = models.CharField(db_column='Tinta', max_length=45, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'impresora'


class Licencia(models.Model):
    idlicencia = models.AutoField(db_column='idLicencia', primary_key=True)  # Field name made lowercase.
    producto = models.CharField(db_column='Producto', max_length=45, blank=True, null=True)  # Field name made lowercase.
    estado = models.IntegerField(db_column='Estado')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'licencia'


class Ordenador(models.Model):
    idordenador = models.ForeignKey(Equipo, models.DO_NOTHING, db_column='idOrdenador', primary_key=True)  # Field name made lowercase.
    tipo = models.CharField(db_column='Tipo', max_length=45, blank=True, null=True)  # Field name made lowercase.
    mac = models.CharField(db_column='MAC', max_length=100, blank=True, null=True)  # Field name made lowercase.
    hostname = models.CharField(db_column='HostName', max_length=100, blank=True, null=True)  # Field name made lowercase.
    procesador = models.CharField(db_column='Procesador', max_length=45, blank=True, null=True)  # Field name made lowercase.
    ram = models.CharField(db_column='RAM', max_length=45, blank=True, null=True)  # Field name made lowercase.
    almacenamiento = models.CharField(db_column='Almacenamiento', max_length=45, blank=True, null=True)  # Field name made lowercase.
    tipo_almacenamiento = models.CharField(db_column='Tipo_Almacenamiento', max_length=10, blank=True, null=True)  # Field name made lowercase.
    os_idos = models.ForeignKey('Os', models.DO_NOTHING, db_column='OS_idOS')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ordenador'


class OrdenadorHasLicencia(models.Model):
    idordenador_has_licencia = models.AutoField(db_column='idOrdenador_Has_Licencia', primary_key=True)  # Field name made lowercase.
    llave = models.CharField(db_column='Llave', max_length=100, blank=True, null=True)  # Field name made lowercase.
    version = models.CharField(max_length=45, blank=True, null=True)
    licencia_idlicencia = models.ForeignKey(Licencia, models.DO_NOTHING, db_column='Licencia_idLicencia')  # Field name made lowercase.
    ordenador_idordenador = models.ForeignKey(Ordenador, models.DO_NOTHING, db_column='Ordenador_idOrdenador')  # Field name made lowercase.
    fecha_instalacion = models.DateField(db_column='Fecha_Instalacion', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ordenador_has_licencia'


class Os(models.Model):
    idos = models.AutoField(db_column='idOS', primary_key=True)  # Field name made lowercase.
    nombre = models.CharField(db_column='Nombre', max_length=100, blank=True, null=True)  # Field name made lowercase.
    servicio = models.CharField(db_column='Servicio', max_length=100, blank=True, null=True)  # Field name made lowercase.
    arquitectura = models.CharField(db_column='Arquitectura', max_length=100, blank=True, null=True)  # Field name made lowercase.
    estado = models.IntegerField(db_column='Estado')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'os'


class OtroDispositivo(models.Model):
    idotro_dispositivo = models.ForeignKey(Equipo, models.DO_NOTHING, db_column='idOtro_Dispositivo', primary_key=True)  # Field name made lowercase.
    nombre = models.CharField(db_column='Nombre', max_length=45, blank=True, null=True)  # Field name made lowercase.
    ordenador_idordenador = models.ForeignKey(Ordenador, models.DO_NOTHING, db_column='Ordenador_idOrdenador', blank=True, null=True)  # Field name made lowercase.
    
    class Meta:
        managed = False
        db_table = 'otro_dispositivo'


class OtroDispositivoHasAtributo(models.Model):
    otro_dispositivo_idotro_dispositivo = models.ForeignKey(OtroDispositivo, models.DO_NOTHING, db_column='Otro_Dispositivo_idOtro_Dispositivo', primary_key=True)  # Field name made lowercase.
    atributo_idatributo = models.ForeignKey(Atributo, models.DO_NOTHING, db_column='Atributo_idAtributo')  # Field name made lowercase.
    detalle = models.CharField(db_column='Detalle', max_length=200, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'otro_dispositivo_has_atributo'
        unique_together = (('otro_dispositivo_idotro_dispositivo', 'atributo_idatributo'),)


class Permiso(models.Model):
    idpermiso = models.AutoField(db_column='idPermiso', primary_key=True)  # Field name made lowercase.
    nombre = models.CharField(db_column='Nombre', max_length=100, blank=True, null=True)  # Field name made lowercase.
    estado = models.IntegerField(db_column='Estado')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'permiso'


class Regional(models.Model):
    idregional = models.AutoField(db_column='idRegional', primary_key=True)  # Field name made lowercase.
    nombre = models.CharField(db_column='Nombre', max_length=45, blank=True, null=True)  # Field name made lowercase.
    estado = models.IntegerField(db_column='Estado')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'regional'


class Tablet(models.Model):
    idtablet = models.ForeignKey(Equipo, models.DO_NOTHING, db_column='idTablet', primary_key=True)  # Field name made lowercase.
    memoria_interna = models.CharField(db_column='Memoria_Interna', max_length=200, blank=True, null=True)  # Field name made lowercase.
    ram = models.CharField(db_column='Ram', max_length=200, blank=True, null=True)  # Field name made lowercase.
    imei = models.CharField(db_column='IMEI', unique=True, max_length=200, blank=True, null=True)  # Field name made lowercase.
    chip = models.CharField(max_length=200, blank=True, null=True)
    camara = models.CharField(db_column='Camara', max_length=200, blank=True, null=True)  # Field name made lowercase.
    procesador = models.CharField(db_column='Procesador', max_length=200, blank=True, null=True)  # Field name made lowercase.
    pantalla = models.CharField(db_column='Pantalla', max_length=200, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tablet'


class Ubicacion(models.Model):
    idubicacion = models.AutoField(db_column='idUbicacion', primary_key=True)  # Field name made lowercase.
    direccion = models.CharField(db_column='Direccion', max_length=200, blank=True, null=True)  # Field name made lowercase.
    edificio = models.CharField(db_column='Edificio', max_length=200, blank=True, null=True)  # Field name made lowercase.
    estado = models.IntegerField(db_column='Estado')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ubicacion'


class UsuarioAd(models.Model):
    idusuario_ad = models.AutoField(db_column='idUsuario_AD', primary_key=True)  # Field name made lowercase.
    nombre = models.CharField(db_column='Nombre', max_length=100, blank=True, null=True)  # Field name made lowercase.
    apellido = models.CharField(db_column='Apellido', max_length=100, blank=True, null=True)  # Field name made lowercase.
    ci = models.CharField(db_column='Ci', max_length=45)  # Field name made lowercase.
    area_idarea = models.ForeignKey(Area, models.DO_NOTHING, db_column='Area_idArea')  # Field name made lowercase.
    empresa_idempresa = models.ForeignKey(Empresa, models.DO_NOTHING, db_column='Empresa_idEmpresa')  # Field name made lowercase.
    gerencia_idgerencia = models.ForeignKey(Gerencia, models.DO_NOTHING, db_column='Gerencia_idGerencia')  # Field name made lowercase.
    regional_idregional = models.ForeignKey(Regional, models.DO_NOTHING, db_column='Regional_idRegional')  # Field name made lowercase.
    ubicacion_idubicacion = models.ForeignKey(Ubicacion, models.DO_NOTHING, db_column='Ubicacion_idUbicacion')  # Field name made lowercase.
    cuenta_idcuenta = models.ForeignKey(Cuenta, models.DO_NOTHING, db_column='Cuenta_idCuenta', blank=True, null=True)  # Field name made lowercase.
    cargo_idcargo = models.ForeignKey(Cargo, models.DO_NOTHING, db_column='Cargo_idCargo')  # Field name made lowercase.
    estado = models.IntegerField(db_column='Estado')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'usuario_ad'


class UsuarioAdHasPermiso(models.Model):
    usuario_ad_idusuario_ad = models.ForeignKey(UsuarioAd, models.DO_NOTHING, db_column='Usuario_AD_idUsuario_AD', primary_key=True)  # Field name made lowercase.
    permiso_idpermiso = models.ForeignKey(Permiso, models.DO_NOTHING, db_column='Permiso_idPermiso')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'usuario_ad_has_permiso'
        unique_together = (('usuario_ad_idusuario_ad', 'permiso_idpermiso'),)


class UsuarioCorreo(models.Model):
    idusuario_correo = models.AutoField(db_column='idUsuario_Correo', primary_key=True)  # Field name made lowercase.
    correo = models.CharField(db_column='Correo', max_length=45, blank=True, null=True)  # Field name made lowercase.
    contrasena = models.CharField(db_column='Contrasena', max_length=45, blank=True, null=True)  # Field name made lowercase.
    tipo = models.CharField(db_column='Tipo', max_length=45, blank=True, null=True)  # Field name made lowercase.
    usuario_ad_idusuario_ad1 = models.ForeignKey(UsuarioAd, models.DO_NOTHING, db_column='Usuario_AD_idUsuario_AD1')  # Field name made lowercase.
    estado = models.IntegerField(db_column='Estado')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'usuario_correo'
