from Sofia_Server.Sofia_App.Modulos.Transacciones.models import Auditoria,Asociacion
from rest_framework import serializers
class AuditoriaSerializer(serializers.ModelSerializer):
    class Meta:
        model=Auditoria
        fields=['idauditoria','id_registro_afectado','tabla_afectada','accion','fecha','ip','usuario_ad_idusuario_ad']

class AsociacionSerializer(serializers.ModelSerializer):
    class Meta:
        model=Asociacion
        fields=['idasociacion','fecha_alta','fecha_baja','motivo','equipo_idequipo','usuarioinicial','usuariofinal']
class AsociacionesNestedSerializer(serializers.ModelSerializer):
    class Meta:
        model=Asociacion
        fields="__all__"
        depth=1