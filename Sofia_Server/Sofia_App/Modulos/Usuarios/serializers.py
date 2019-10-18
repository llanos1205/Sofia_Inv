from rest_framework import serializers
from Sofia_Server.Sofia_App.Modulos.Usuarios.models import UsuarioAdHasPermiso,UsuarioAd,Cuenta,UsuarioCorreo,Permiso
from Sofia_Server.Sofia_App.Modulos.InfoUser.serializers import PermisoSerializer
class UsuarioMinisSerializer(serializers.ModelSerializer):
    class Meta:
        model=UsuarioAd
        fields=['idusuario_ad','nombre','apellido','ci']

class UsuarioADSerializer(serializers.ModelSerializer):
    permisos= serializers.PrimaryKeyRelatedField(many=True, read_only=False, queryset=Permiso.objects.all())
    class Meta:
        model=UsuarioAd
        fields="__all__"
        depth=0
        
class UsuarioADSerializerFull(serializers.ModelSerializer):
    permisos=PermisoSerializer(many=True,read_only=True)
    class Meta:
        model=UsuarioAd
        fields="__all__"
        depth=2
class CuentaSerializer(serializers.ModelSerializer):
    Usuarios=UsuarioADSerializer(many=True,read_only=True)
    class Meta:
        model=Cuenta
        fields="__all__"
class UsuarioCorreoSerializer(serializers.ModelSerializer):
    
    class Meta:
        model=UsuarioCorreo
        fields=['idusuario_correo','correo','contrasena',
                'tipo','usuario_ad_idusuario_ad1','estado']
class Permiso_UsuarioADSerializer(serializers.ModelSerializer):
    usuario_ad_idusuario_ad=serializers.PrimaryKeyRelatedField(many=False, read_only=False, queryset=UsuarioAd.objects.all())
    class Meta:
        model=UsuarioAdHasPermiso
        fields=['usuario_ad_idusuario_ad','permiso_idpermiso']


class CorreoNestedSerializer(serializers.ModelSerializer):
    class Meta:
        model=UsuarioCorreo
        fields="__all__"
        depth=1
