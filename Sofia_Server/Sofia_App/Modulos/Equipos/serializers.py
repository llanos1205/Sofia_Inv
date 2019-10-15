
from Sofia_Server.Sofia_App.Modulos.Equipos.models import (OrdenadorHasLicencia,Atributo,Tablet,
Equipo,Ordenador,Impresora,OtroDispositivo,OtroDispositivoHasAtributo,Licencia,Os)
from rest_framework import serializers
class FilteredListSerializer(serializers.ListSerializer):

    def to_representation(self, data):
        data = data.filter(user=self.request.user, edition__hide=False)
        return super(FilteredListSerializer, self).to_representation(data)

class AtributoSerialzier(serializers.ModelSerializer):
    class Meta:
        model=Atributo

        fields=['idatributo','nombre','estado']
class EquipoSerializer(serializers.ModelSerializer):
    class Meta:
        model=Equipo
        fields="__all__"
class OrdenadorSerializer(serializers.ModelSerializer):
    perifericos=serializers.PrimaryKeyRelatedField(many=True,read_only=True)
    os_idos=serializers.PrimaryKeyRelatedField(many=False,read_only=False,queryset=Os.objects.all())
    class Meta:
        model=Ordenador
        fields="__all__"
        depth=2
        
class ImpresoraSerializer(serializers.ModelSerializer):
    class Meta:
        model=Impresora
        fields="__all__"
class OtroDispositivoSerializer(serializers.ModelSerializer):
    atributos= serializers.PrimaryKeyRelatedField(many=True, read_only=False, queryset=Atributo.objects.all())
    class Meta:
        model=OtroDispositivo
        fields="__all__"
class LicenciaSerializer(serializers.ModelSerializer):
    class Meta:
        model=Licencia
        fields=['idlicencia','producto','estado']
class OtroDispositivoHasAtributoSerializer(serializers.ModelSerializer):
    otro_dispositivo_idotro_dispositivo= serializers.PrimaryKeyRelatedField(many=False,read_only=False,queryset=OtroDispositivo.objects.all())
    class Meta:
        model=OtroDispositivoHasAtributo
        fields="__all__"
class OsSerializer(serializers.ModelSerializer):
    class Meta:
        model=Os
        fields=['idos','nombre','servicio','arquitectura','estado']

class EquipoNestedSerializer(serializers.ModelSerializer):
    class Meta:
        model=Equipo
        fields="__all__"
        depth=2

class OrdenadorNestedSerializer(serializers.ModelSerializer):
    perifericos=serializers.PrimaryKeyRelatedField(many=True,read_only=True)
    idordenador=EquipoNestedSerializer()
    class Meta:
        model=Ordenador
        fields="__all__"
        depth=2
class ImpresoraNestedSerializer(serializers.ModelSerializer):
    idimpresora=EquipoNestedSerializer()
    class Meta:
        model=Impresora
        fields="__all__"
        depth=2

class OtrosDispositivosNestedSerializer(serializers.ModelSerializer):
    idotro_dispositivo=EquipoNestedSerializer()
    atributos=AtributoSerialzier(many=True,read_only=True)
    class Meta:
        model=OtroDispositivo
        fields="__all__"
        depth=2
class OrdenadorHasLicenciaSerializer(serializers.ModelSerializer):
    class Meta:
        model=OrdenadorHasLicencia
        fields=['idordenador_has_licencia','llave','version','fecha_instalacion','licencia_idlicencia','ordenador_idordenador']
class TabletSerializer(serializers.ModelSerializer):
    class Meta:
        model=Tablet
        fields="__all__"