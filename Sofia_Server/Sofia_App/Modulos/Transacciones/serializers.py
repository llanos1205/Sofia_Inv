from Sofia_Server.Sofia_App.Modulos.Transacciones.models import Auditoria,Asociacion
from rest_framework import serializers
class AuditoriaSerializer(serializers.ModelSerializer):
    class Meta:
        model=Auditoria
        fields="__all__"
class AuditoriaNestedSerializer(serializers.ModelSerializer):
    class Meta:
        model=Auditoria
        fields="__all__"
        depth=1
class AsociacionSerializer(serializers.ModelSerializer):
    class Meta:
        model=Asociacion
        fields="__all__"
class AsociacionesNestedSerializer(serializers.ModelSerializer):
    class Meta:
        model=Asociacion
        fields="__all__"
        depth=1