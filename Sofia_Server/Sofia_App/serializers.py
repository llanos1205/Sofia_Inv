from django.contrib.auth.models import User, Group
from Sofia_Server.Sofia_App.models import Equipo,UsuarioAd,Empresa,Area,Departamento,Ubicacion,Gerencia,Regional
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
        fields=['idequipo','marca','modelo','nro_serie','nro_activo_fijo','ip','ultima_observacion']
class EmpresaSerializer(serializers.ModelSerializer):
    class Meta:
        model=Empresa
        fields=['idempresa','nombre','descripcion','estado']
class DepartamentoSerializer(serializers.ModelSerializer):
    areas=serializers.PrimaryKeyRelatedField(many=True,read_only=True)
    class Meta:
        model=Departamento
        fields=['iddepartamento','nombre','descripcion','estado','areas']
class AreaSerializer(serializers.ModelSerializer):
    class Meta:
        model=Area
        fields=['idarea','nombre','descripcion','departamento_iddepartamento','estado']

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
