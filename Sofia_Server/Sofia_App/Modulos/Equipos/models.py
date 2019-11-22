from django.db import models

class Atributo(models.Model):
    idatributo = models.AutoField(db_column='idAtributo', primary_key=True)  # Field name made lowercase.
    nombre = models.CharField(db_column='Nombre', max_length=200, blank=True, null=True)  # Field name made lowercase.
    estado = models.IntegerField(db_column='Estado')  # Field name made lowercase.
    class Meta:
        managed = False
        db_table = 'atributo'
    def __str__(self):
        return '%d: %s' % (self.idatributo, self.nombre)
class Equipo(models.Model):
    idequipo = models.AutoField(db_column='idEquipo',primary_key=True)  # Field name made lowercase.
    marca = models.CharField(db_column='Marca', max_length=200, blank=True, null=True)  # Field name made lowercase.
    modelo = models.CharField(db_column='Modelo', max_length=200, blank=True, null=True)  # Field name made lowercase.
    nro_serie = models.CharField(db_column='Nro_Serie', max_length=200, blank=True, null=True)  # Field name made lowercase.
    nro_activo_fijo = models.CharField(db_column='Nro_Activo_Fijo', max_length=200, blank=True, null=True)  # Field name made lowercase.
    ip = models.CharField(db_column='Ip', max_length=200, blank=True, null=True)  # Field name made lowercase.
    ultima_observacion = models.CharField(db_column='Ultima_Observacion', max_length=200, blank=True, null=True)  # Field name made lowercase.
    usuarios=models.ManyToManyField('UsuarioAd',related_name='usuarios',through='Asociacion',through_fields=('equipo_idequipo','usuariofinal'))
    estado = models.IntegerField(db_column='Estado')  # Field name made lowercase.
    class Meta:
        managed = False
        db_table = 'equipo'
    def __str__(self):
        return '%d:%s'%(self.idequipo,self.nro_serie)    
class Impresora(Equipo):
    idimpresora = models.OneToOneField(Equipo, models.CASCADE,  primary_key=True,db_column='idImpresora', parent_link=True)  # Field name made lowercase.
    tipo = models.CharField(db_column='Tipo', max_length=45, blank=True, null=True)  # Field name made lowercase.
    tinta = models.CharField(db_column='Tinta', max_length=45, blank=True, null=True)  # Field name made lowercase.
    class Meta:
        managed = False
        db_table = 'impresora'
    def __str__(self):
        return '(Impresora) %s: %s' % (self.idimpresora, self.tipo)
class Licencia(models.Model):
    idlicencia = models.AutoField(db_column='idLicencia', primary_key=True)  # Field name made lowercase.
    producto = models.CharField(db_column='Producto', max_length=45, blank=True, null=True)  # Field name made lowercase.
    estado = models.IntegerField(db_column='Estado')  # Field name made lowercase.
    class Meta:
        managed = False
        db_table = 'licencia'
    def __str__(self):
        return '%d: %s' % (self.idlicencia, self.producto)
class Os(models.Model):
    idos = models.AutoField(db_column='idOS', primary_key=True)  # Field name made lowercase.
    nombre = models.CharField(db_column='Nombre', max_length=200, blank=True, null=True)  # Field name made lowercase.
    servicio = models.CharField(db_column='Servicio', max_length=200, blank=True, null=True)  # Field name made lowercase.
    arquitectura = models.CharField(db_column='Arquitectura', max_length=200, blank=True, null=True)  # Field name made lowercase.
    estado = models.IntegerField(db_column='Estado')  # Field name made lowercase.
    class Meta:
        managed = False
        db_table = 'os'
    def __str__(self):
        return '%d: %s' % (self.idos, self.nombre)

class Ordenador(Equipo):
    idordenador = models.OneToOneField(Equipo, models.CASCADE,parent_link=True, db_column='idOrdenador',primary_key=True,related_name='ordenadores')  # Field name made lowercase.
    tipo = models.CharField(db_column='Tipo', max_length=200, blank=True, null=True)  # Field name made lowercase.
    mac = models.CharField(db_column='MAC', max_length=200, blank=True, null=True)  # Field name made lowercase.
    hostname = models.CharField(db_column='HostName', max_length=200, blank=True, null=True)  # Field name made lowercase.
    procesador = models.CharField(db_column='Procesador', max_length=200, blank=True, null=True)  # Field name made lowercase.
    ram = models.CharField(db_column='RAM', max_length=200, blank=True, null=True)  # Field name made lowercase.
    almacenamiento = models.CharField(db_column='Almacenamiento', max_length=200, blank=True, null=True)  # Field name made lowercase.
    tipo_almacenamiento = models.CharField(db_column='Tipo_Almacenamiento', max_length=200, blank=True, null=True)  # Field name made lowercase.
    os_idos = models.ForeignKey(Os, models.SET_NULL, db_column='OS_idOS',null=True)  # Field name made lowercase.
    class Meta:
        managed = False
        db_table = 'ordenador'
    def __str__(self):
        return '(ordenador) %s: %s' % (self.idordenador, self.tipo)
class OrdenadorHasLicencia(models.Model):
    idordenador_has_licencia = models.AutoField(db_column='idOrdenador_Has_Licencia', primary_key=True)  # Field name made lowercase.
    llave = models.CharField(db_column='Llave', max_length=200, blank=True, null=True)  # Field name made lowercase.
    version = models.CharField(max_length=200, blank=True, null=True)
    licencia_idlicencia = models.ForeignKey(Licencia, models.SET_NULL, db_column='Licencia_idLicencia',null=True)  # Field name made lowercase.
    ordenador_idordenador = models.ForeignKey(Ordenador, models.SET_NULL, db_column='Ordenador_idOrdenador',blank=True,null=True)  # Field name made lowercase.
    fecha_instalacion = models.DateField(db_column='Fecha_Instalacion', blank=True, null=True)  # Field name made lowercase.
    class Meta:
        managed = False
        db_table = 'ordenador_has_licencia'
class OtroDispositivo(Equipo):
    idotro_dispositivo = models.OneToOneField(Equipo, models.CASCADE,parent_link=True, db_column='idOtro_Dispositivo', primary_key=True)  # Field name made lowercase.
    nombre = models.CharField(db_column='Nombre', max_length=200, blank=True, null=True)  # Field name made lowercase.
    ordenador_idordenador = models.ForeignKey(Ordenador, models.SET_NULL, db_column='Ordenador_idOrdenador', blank=True, null=True,related_name='perifericos')  # Field name made lowercase.
    atributos=models.ManyToManyField(Atributo,related_name='atributos',through='OtroDispositivoHasAtributo',blank=True,null=True)
    class Meta:
        managed = False
        db_table = 'otro_dispositivo'
    def __str__(self):
        return '(otro dispositivo) %s: %s' % (self.idotro_dispositivo, self.nombre)
class OtroDispositivoHasAtributo(models.Model):
    idotro_dispositivo_has_atributo=models.AutoField(db_column="idOtro_Dispositivo_has_Atributo",primary_key=True)
    otro_dispositivo_idotro_dispositivo = models.ForeignKey(OtroDispositivo, models.DO_NOTHING, db_column='Otro_Dispositivo_idOtro_Dispositivo')  # Field name made lowercase.
    atributo_idatributo = models.ForeignKey(Atributo, models.DO_NOTHING, db_column='Atributo_idAtributo')  # Field name made lowercase.
    detalle = models.CharField(db_column='Detalle', max_length=200, blank=True, null=True)  # Field name made lowercase.
    class Meta:
        managed = False
        db_table = 'otro_dispositivo_has_atributo'

class Tablet(Equipo):
    idtablet = models.OneToOneField(Equipo, models.CASCADE, db_column='idTablet',parent_link=True, primary_key=True)  # Field name made lowercase.
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
    def __str__(self):
        return '(tablet  )%d: %s' % (self.idtablet, self.imei)
