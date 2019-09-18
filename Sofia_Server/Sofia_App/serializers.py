from django.contrib.auth.models import User, Group
from Sofia_Server.Sofia_App.models import Equipo,UsuarioAd,Empresa
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
class EquipoSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model=Equipo
        fields=['idequipo','marca','modelo','nro_serie','nro_activo_fijo','ip','ultima_observacion']
class EmpresaSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model=Empresa
        fields=['idempresa','nombre','descripcion']