from Sofia_Server.Sofia_App.Modulos.Transacciones.models import Auditoria,Asociacion
from rest_framework import serializers
from Sofia_Server.Sofia_App.Modulos.Usuarios import serializers as userser
class AuditoriaSerializer(serializers.ModelSerializer):
    class Meta:
        model=Auditoria
        fields="__all__"
class AuditoriaNestedSerializer(serializers.ModelSerializer):
    usuario_ad_idusuario_ad=userser.UsuarioMinisSerializer()
    class Meta:
        model=Auditoria
        fields="__all__"
        depth=1
class AsociacionSerializer(serializers.ModelSerializer):
    #usuariofinal=userser.UsuarioMinisSerializer(read_only=True)
    class Meta:
        model=Asociacion
        fields="__all__"
        
class AsociacionesNestedSerializer(serializers.ModelSerializer):
    usuariofinal=userser.UsuarioMinisSerializer()
    class Meta:
        model=Asociacion
        fields="__all__"
        depth=2