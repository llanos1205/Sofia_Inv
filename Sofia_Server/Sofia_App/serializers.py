from django.contrib.auth.models import User, Group
from Sofia_Server.Sofia_App.models import (Equipo,UsuarioAd,
                                            Empresa,Area,Departamento,Ubicacion,
                                            Gerencia,Regional,UsuarioAd,Cargo,
                                            Cuenta,UsuarioCorreo,Equipo,Ordenador,
                                            Impresora,OtroDispositivo,Atributo,Permiso,
                                            UsuarioAdHasPermiso,Licencia,Os,Atributo,
                                            EquipoHasAtributo,Auditoria,Asociacion,OrdenadorHasLicencia)
from rest_framework import serializers


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'groups']


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ['url', 'name']
class UsuarioAdSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model=UsuarioAd
        fields=['idusuario_ad','nombre','apellido']
class EquipoSerializer(serializers.ModelSerializer):
    class Meta:
        model=Equipo
        fields=['idequipo','marca','modelo','nro_serie',
                'nro_activo_fijo','ip','ultima_observacion',
                'usuario_ad_idusuario_ad','estado']
class EmpresaSerializer(serializers.ModelSerializer):
    class Meta:
        model=Empresa
        fields=['idempresa','nombre','descripcion','estado']
class DepartamentoSerializer(serializers.ModelSerializer):
    areas=serializers.PrimaryKeyRelatedField(many=True,read_only=True)
    class Meta:
        model=Departamento
        fields=['iddepartamento','nombre',
                'descripcion','estado','areas']
class AreaSerializer(serializers.ModelSerializer):
    class Meta:
        model=Area
        fields=['idarea','nombre','descripcion',
                'departamento_iddepartamento','estado']

class RegionalSerializer(serializers.ModelSerializer):
    class Meta:
        model=Regional
        fields=['idregional','nombre','estado']

class UbicacionSerializer(serializers.ModelSerializer):
    class Meta:
        model=Ubicacion
        fields=['idubicacion','direccion','edificio','estado']
class GerenciaSerializer(serializers.ModelSerializer):
    class Meta:
        model=Gerencia
        fields=['idgerencia','nombre','descripcion','estado']
class CargoSerializer(serializers.ModelSerializer):
    class Meta:
        model=Cargo
        fields=['idcargo','nombre','descripcion','estado']
class PermisoSerializer(serializers.ModelSerializer):
    class Meta:
        model=Permiso
        fields=['idpermiso','nombre','estado']
class UsuarioADSerializer(serializers.ModelSerializer):
    permisos= serializers.PrimaryKeyRelatedField(many=True, read_only=False, queryset=Permiso.objects.all())
    class Meta:
        model=UsuarioAd
        fields=['idusuario_ad','nombre','apellido','ci','area_idarea',
                'empresa_idempresa','gerencia_idgerencia','regional_idregional',
                'ubicacion_idubicacion','cuenta_idcuenta','cargo_idcargo','permisos','estado']
        depth=0
        
class UsuarioADSerializerFull(serializers.ModelSerializer):
    permisos=PermisoSerializer(many=True,read_only=True)
    class Meta:
        model=UsuarioAd
        fields=['idusuario_ad','nombre','apellido','ci','area_idarea',
                'empresa_idempresa','gerencia_idgerencia','regional_idregional',
                'ubicacion_idubicacion','cuenta_idcuenta','cargo_idcargo','permisos','estado']
        depth=2
class CuentaSerializer(serializers.ModelSerializer):
    class Meta:
        model=Cuenta
        fields=['idcuenta','usuario','contrasena','estado']
class UsuarioCorreoSerializer(serializers.ModelSerializer):
    
    class Meta:
        model=UsuarioCorreo
        fields=['idusuario_correo','correo','contrasena',
                'tipo','usuario_ad_idusuario_ad1','estado']
class AtributoSerialzier(serializers.ModelSerializer):
    class Meta:
        model=Atributo
        fields=['idatributo','nombre','estado']
class EquipoSerializer(serializers.ModelSerializer):
    atributos= serializers.PrimaryKeyRelatedField(many=True, read_only=False, queryset=Atributo.objects.all())
    class Meta:
        model=Equipo
        fields=['idequipo','marca','modelo','nro_serie',
                'nro_activo_fijo','ip','ultima_observacion',
                'usuario_ad_idusuario_ad','atributos','estado']


class Permiso_UsuarioADSerializer(serializers.ModelSerializer):
    usuario_ad_idusuario_ad=serializers.PrimaryKeyRelatedField(many=False, read_only=False, queryset=UsuarioAd.objects.all())
    class Meta:
        model=UsuarioAdHasPermiso
        fields=['usuario_ad_idusuario_ad','permiso_idpermiso']
class OrdenadorSerializer(serializers.ModelSerializer):
    perifericos=serializers.PrimaryKeyRelatedField(many=True,read_only=True)
    class Meta:
        model=Ordenador
        fields=['idordenador','tipo','mac','hostname',
                'procesador','ram','almacenamiento','tipo_almacenamiento','perifericos','os_idos']
        
class ImpresoraSerializer(serializers.ModelSerializer):
    class Meta:
        model=Impresora
        fields=['idimpresora','tipo','tinta']
class OtroDispositivoSerializer(serializers.ModelSerializer):
    class Meta:
        model=OtroDispositivo
        fields=['idotro_dispositivo','nombre','ordenador_idordenador']
class LicenciaSerializer(serializers.ModelSerializer):
    class Meta:
        model=Licencia
        fields=['idlicencia','producto','estado']
class EquipoHasAtributoSerializer(serializers.ModelSerializer):
    equipo_idequipo=serializers.PrimaryKeyRelatedField(many=False, read_only=False, queryset=Equipo.objects.all())
    class Meta:
        model=EquipoHasAtributo
        fields=['equipo_idequipo','atributo_idatributo','descripcion']

class OsSerializer(serializers.ModelSerializer):
    class Meta:
        model=Os
        fields=['idos','nombre','servicio','arquitectura','estado']

class AuditoriaSerializer(serializers.ModelSerializer):
    class Meta:
        model=Auditoria
        fields=['idauditoria','id_registro_afectado','tabla_afectada','accion','fecha','ip','usuario_ad_idusuario_ad']

class AsociacionSerializer(serializers.ModelSerializer):
    class Meta:
        model=Asociacion
        fields=['idasociacion','fecha_alta','fecha_baja','motivo','equipo_idequipo','usuarioinicial','usuariofinal']
class OrdenadorHasLicenciaSerializer(serializers.ModelSerializer):
    class Meta:
        model=OrdenadorHasLicencia
        fields=['idordenador_has_licencia','llave','version','fecha_instalacion','licencia_idlicencia','ordenador_idordenador']