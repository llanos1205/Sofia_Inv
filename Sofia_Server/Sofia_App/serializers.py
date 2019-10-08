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
# class EquipoSerializer(serializers.ModelSerializer):
#     class Meta:
#         model=Equipo
#         fields=['idequipo','marca','modelo','nro_serie',
#                 'nro_activo_fijo','ip','ultima_observacion',
#                 'usuario_ad_idusuario_ad','estado']



