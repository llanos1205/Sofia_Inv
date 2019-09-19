from django.contrib.auth.models import User, Group
from Sofia_Server.Sofia_App.models import (Equipo,UsuarioAd,
                                            Empresa,Area,Departamento,Ubicacion,
                                            Gerencia,Regional,UsuarioAd,Cargo,
                                            Cuenta,UsuarioCorreo,Equipo,Ordenador,
                                            Impresora,OtroDispositivo,Atributo,Permiso,
                                            UsuarioAdHasPermiso)
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
                'nro_activo_fijo','ip','ultima_observacion']
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
class UsuarioADSerializer(serializers.ModelSerializer):
    class Meta:
        model=UsuarioAd
        fields=['idusuario_ad','nombre','apellido','area_idarea',
                'empresa_idempresa','gerencia_idgerencia','regional_idregional',
                'ubicacion_idubicacion','cuenta_idcuenta','cargo_idcargo','estado']
class CuentaSerializer(serializers.ModelSerializer):
    class Meta:
        model=Cuenta
        fields=['idcuenta','usuario','contrasena','estado']
class UsuarioCorreoSerializer(serializers.ModelSerializer):
    class Meta:
        model=UsuarioCorreo
        fields=['idusuario_correo','correo','contrasena',
                'tipo','usuario_ad_idusuario_ad1','estado']
class EquipoSerializer(serializers.ModelSerializer):
    class Meta:
        model=Equipo
        fields=['idequipo','marca','modelo','nro_serie',
                'nro_activo_fijo','ip','ultima_observacion',
                'usuario_ad_idusuario_ad','estado']
class PermisoSerializer(serializers.ModelSerializer):
    class Meta:
        model=Permiso
        fields=['idpermiso','nombre','estado']

class Permiso_UsuarioADSerializer(serializers.ModelSerializer):
    class Meta:
        model=UsuarioAdHasPermiso
        fields=['usuario_ad_idusuario_ad','permiso_idpermiso']