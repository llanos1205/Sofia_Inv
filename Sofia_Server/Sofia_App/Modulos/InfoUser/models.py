from django.db import models
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
