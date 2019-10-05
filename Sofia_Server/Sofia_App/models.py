from django.db import models

# Create your models here.

class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.IntegerField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.PositiveSmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'
        ########################3

class Area(models.Model):
    idarea = models.AutoField(db_column='idArea', primary_key=True)  # Field name made lowercase.
    nombre = models.CharField(db_column='Nombre', max_length=45, blank=True, null=True)  # Field name made lowercase.
    descripcion = models.CharField(db_column='Descripcion', max_length=100, blank=True, null=True)  # Field name made lowercase.
    departamento_iddepartamento = models.ForeignKey('Departamento', models.DO_NOTHING, db_column='Departamento_idDepartamento',related_name='areas')  # Field name made lowercase.
    estado = models.IntegerField(db_column='Estado')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'area'
    def __str__(self):
        return '%d: %s' % (self.idarea, self.nombre)

class Asociacion(models.Model):
    idasociacion = models.AutoField(db_column='idAsociacion', primary_key=True)  # Field name made lowercase.
    fecha_alta = models.DateField(db_column='Fecha_Alta', blank=True, null=True)  # Field name made lowercase.
    fecha_baja = models.DateField(db_column='Fecha_Baja', blank=True, null=True)  # Field name made lowercase.
    motivo = models.CharField(db_column='Motivo', max_length=75, blank=True, null=True)  # Field name made lowercase.
    equipo_idequipo = models.ForeignKey('Equipo', models.DO_NOTHING,db_column='Equipo_idEquipo')  # Field name made lowercase.
    usuarioinicial = models.ForeignKey('UsuarioAd', models.DO_NOTHING,related_name='inicial', db_column='UsuarioInicial', blank=True, null=True)  # Field name made lowercase.
    usuariofinal = models.ForeignKey('UsuarioAd', models.DO_NOTHING,related_name='final', db_column='UsuarioFInal', blank=True, null=True)  # Field name made lowercase.

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
    def __str__(self):
        return '%d: %s' % (self.idatributo, self.nombre)
    
class Auditoria(models.Model):
    idauditoria = models.AutoField(db_column='idAuditoria', primary_key=True)  # Field name made lowercase.
    id_registro_afectado = models.IntegerField(db_column='Id_Registro_Afectado', blank=True, null=True)  # Field name made lowercase.
    tabla_afectada = models.CharField(db_column='Tabla_Afectada', max_length=45, blank=True, null=True)  # Field name made lowercase.
    accion = models.CharField(db_column='Accion', max_length=45, blank=True, null=True)  # Field name made lowercase.
    fecha = models.DateField(db_column='Fecha', blank=True, null=True)  # Field name made lowercase.
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
    def __str__(self):
        return '%d: %s' % (self.idcargo, self.nombre)

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

class Departamento(models.Model):
    iddepartamento = models.AutoField(db_column='idDepartamento', primary_key=True)  # Field name made lowercase.
    nombre = models.CharField(db_column='Nombre', max_length=45, blank=True, null=True)  # Field name made lowercase.
    descripcion = models.CharField(db_column='Descripcion', max_length=100, blank=True, null=True)  # Field name made lowercase.
    estado = models.IntegerField(db_column='Estado')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'departamento'
    def __str__(self):
        return '%d: %s' % (self.iddepartamento, self.nombre)

class Empresa(models.Model):
    idempresa = models.AutoField(db_column='idEmpresa', primary_key=True)  # Field name made lowercase.
    nombre = models.CharField(db_column='Nombre', max_length=45, blank=True, null=True)  # Field name made lowercase.
    descripcion = models.CharField(db_column='Descripcion', max_length=100, blank=True, null=True)  # Field name made lowercase.
    estado = models.IntegerField(db_column='Estado')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'empresa'
    def __str__(self):
        return '%d:%s'%(self.idempresa,self.nombre)

class Equipo(models.Model):
    idequipo = models.AutoField(db_column='idEquipo', primary_key=True)  # Field name made lowercase.
    marca = models.CharField(db_column='Marca', max_length=100, blank=True, null=True)  # Field name made lowercase.
    modelo = models.CharField(db_column='Modelo', max_length=100, blank=True, null=True)  # Field name made lowercase.
    nro_serie = models.CharField(db_column='Nro_Serie', max_length=100, blank=True, null=True)  # Field name made lowercase.
    nro_activo_fijo = models.CharField(db_column='Nro_Activo_Fijo', max_length=100, blank=True, null=True)  # Field name made lowercase.
    ip = models.CharField(db_column='Ip', max_length=18, blank=True, null=True)  # Field name made lowercase.
    ultima_observacion = models.CharField(db_column='Ultima_Observacion', max_length=45, blank=True, null=True)  # Field name made lowercase.
    usuario_ad_idusuario_ad = models.ForeignKey('UsuarioAd', models.DO_NOTHING, db_column='Usuario_AD_idUsuario_AD', blank=True, null=True)  # Field name made lowercase.
    estado = models.IntegerField(db_column='Estado')  # Field name made lowercase.
    atributos=models.ManyToManyField(Atributo,related_name='atributos',through='EquipoHasAtributo')
  
    class Meta:
        managed = False
        db_table = 'equipo'
    def __str__(self):
        return '%d:%s'%(self.idequipo,self.nro_serie)    

class EquipoHasAtributo(models.Model):
    equipo_idequipo = models.ForeignKey(Equipo, models.DO_NOTHING, db_column='Equipo_idEquipo', primary_key=True)  # Field name made lowercase.
    atributo_idatributo = models.ForeignKey(Atributo, models.DO_NOTHING, db_column='Atributo_idAtributo')  # Field name made lowercase.
    descripcion = models.CharField(db_column='Descripcion', max_length=100, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'equipo_has_atributo'
        unique_together = (('equipo_idequipo', 'atributo_idatributo'),)

class Gerencia(models.Model):
    idgerencia = models.AutoField(db_column='idGerencia', primary_key=True)  # Field name made lowercase.
    nombre = models.CharField(db_column='Nombre', max_length=45, blank=True, null=True)  # Field name made lowercase.
    descripcion = models.CharField(db_column='Descripcion', max_length=100, blank=True, null=True)  # Field name made lowercase.
    estado = models.IntegerField(db_column='Estado')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'gerencia'
    def __str__(self):
        return '%d: %s' % (self.idgerencia, self.nombre)

class Impresora(models.Model):
    idimpresora = models.OneToOneField(Equipo, models.DO_NOTHING, db_column='idImpresora', primary_key=True)  # Field name made lowercase.
    tipo = models.CharField(db_column='Tipo', max_length=45, blank=True, null=True)  # Field name made lowercase.
    tinta = models.CharField(db_column='Tinta', max_length=45, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'impresora'
    def __str__(self):
        return '%d: %s' % (self.idcargo, self.tipo)

class Licencia(models.Model):
    idlicencia = models.AutoField(db_column='idLicencia', primary_key=True)  # Field name made lowercase.
    producto = models.CharField(db_column='Producto', max_length=45, blank=True, null=True)  # Field name made lowercase.
    estado = models.IntegerField(db_column='Estado')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'licencia'
    def __str__(self):
        return '%d: %s' % (self.idlicencia, self.producto)

class Ordenador(models.Model):
    idordenador = models.OneToOneField(Equipo, models.DO_NOTHING, db_column='idOrdenador',primary_key=True)  # Field name made lowercase.
    tipo = models.CharField(db_column='Tipo', max_length=45, blank=True, null=True)  # Field name made lowercase.
    mac = models.CharField(db_column='MAC', max_length=100, blank=True, null=True)  # Field name made lowercase.
    hostname = models.CharField(db_column='HostName', max_length=100, blank=True, null=True)  # Field name made lowercase.
    procesador = models.CharField(db_column='Procesador', max_length=45, blank=True, null=True)  # Field name made lowercase.
    ram = models.CharField(db_column='RAM', max_length=10, blank=True, null=True)  # Field name made lowercase.
    almacenamiento = models.CharField(db_column='Almacenamiento', max_length=45, blank=True, null=True)  # Field name made lowercase.
    tipo_almacenamiento = models.CharField(db_column='Tipo_Almacenamiento', max_length=10, blank=True, null=True)  # Field name made lowercase.
    os_idos = models.ForeignKey('Os', models.DO_NOTHING, db_column='OS_idOS',related_name='Sistema_Operativo')  # Field name made lowercase.
    

    class Meta:
        managed = False
        db_table = 'ordenador'
    def __str__(self):
        return '%s: %s' % (self.idordenador, self.tipo)

class OrdenadorHasLicencia(models.Model):
    idordenador_has_licencia = models.AutoField(db_column='idOrdenador_Has_Licencia', primary_key=True)  # Field name made lowercase.
    llave = models.CharField(db_column='Llave', max_length=100, blank=True, null=True)  # Field name made lowercase.
    version = models.CharField(max_length=45, blank=True, null=True)
    licencia_idlicencia = models.ForeignKey(Licencia, models.DO_NOTHING, db_column='Licencia_idLicencia')  # Field name made lowercase.
    ordenador_idordenador = models.ForeignKey(Ordenador, models.DO_NOTHING, db_column='Ordenador_idOrdenador',blank=True,null=True)  # Field name made lowercase.
    fecha_instalacion = models.DateTimeField(db_column='Fecha_Instalacion', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ordenador_has_licencia'

class Os(models.Model):
    idos = models.AutoField(db_column='idOS', primary_key=True)  # Field name made lowercase.
    nombre = models.CharField(db_column='Nombre', max_length=25, blank=True, null=True)  # Field name made lowercase.
    servicio = models.CharField(db_column='Servicio', max_length=20, blank=True, null=True)  # Field name made lowercase.
    arquitectura = models.CharField(db_column='Arquitectura', max_length=5, blank=True, null=True)  # Field name made lowercase.
    estado = models.IntegerField(db_column='Estado')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'os'
    def __str__(self):
        return '%d: %s' % (self.idos, self.nombre)

class OtroDispositivo(models.Model):
    idotro_dispositivo = models.OneToOneField(Equipo, models.DO_NOTHING, db_column='idOtro_Dispositivo', primary_key=True)  # Field name made lowercase.
    nombre = models.CharField(db_column='Nombre', max_length=45, blank=True, null=True)  # Field name made lowercase.
    ordenador_idordenador = models.ForeignKey(Ordenador, models.DO_NOTHING, db_column='Ordenador_idOrdenador', blank=True, null=True,related_name='perifericos')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'otro_dispositivo'
    def __str__(self):
        return '%d: %s' % (self.idotro_dispositivo, self.nombre)

class Permiso(models.Model):
    idpermiso = models.AutoField(db_column='idPermiso', primary_key=True)  # Field name made lowercase.
    nombre = models.CharField(db_column='Nombre', max_length=100, blank=True, null=True)  # Field name made lowercase.
    estado = models.IntegerField(db_column='Estado')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'permiso'
    def __str__(self):
        return '%d: %s' % (self.idpermiso, self.nombre)

class Regional(models.Model):
    idregional = models.AutoField(db_column='idRegional', primary_key=True)  # Field name made lowercase.
    nombre = models.CharField(db_column='Nombre', max_length=45, blank=True, null=True)  # Field name made lowercase.
    estado = models.IntegerField(db_column='Estado')  # Field name made lowercase.
    class Meta:
        managed = False
        db_table = 'regional'
    def __str__(self):
        return '%d: %s' % (self.idregional, self.nombre)

class Ubicacion(models.Model):
    idubicacion = models.AutoField(db_column='idUbicacion', primary_key=True)  # Field name made lowercase.
    direccion = models.CharField(db_column='Direccion', max_length=200, blank=True, null=True)  # Field name made lowercase.
    edificio = models.CharField(db_column='Edificio', max_length=200, blank=True, null=True)  # Field name made lowercase.
    estado = models.IntegerField(db_column='Estado')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ubicacion'
    def __str__(self):
        return '%d: %s' % (self.idubicacion, self.direccion)

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
    cuenta_idcuenta = models.ForeignKey(Cuenta, models.DO_NOTHING, db_column='Cuenta_idCuenta',null=True)  # Field name made lowercase.
    cargo_idcargo = models.ForeignKey(Cargo, models.DO_NOTHING, db_column='Cargo_idCargo')  # Field name made lowercase.
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
    usuario_ad_idusuario_ad1 = models.ForeignKey(UsuarioAd, models.DO_NOTHING, db_column='Usuario_AD_idUsuario_AD1')  # Field name made lowercase.
    estado = models.IntegerField(db_column='Estado')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'usuario_correo'
    def __str__(self):
        return '%d: %s' % (self.idusuario_correo, self.correo)