
from Sofia_Server.Sofia_App.Modulos.Equipos.models import (OrdenadorHasLicencia,Atributo,Tablet,
Equipo,Ordenador,Impresora,OtroDispositivo,OtroDispositivoHasAtributo,Licencia,Os)
from rest_framework import serializers
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
        fields=['idimpresora','tipo','tinta']
class OtroDispositivoSerializer(serializers.ModelSerializer):
    class Meta:
        model=OtroDispositivo
        fields=['idotro_dispositivo','nombre','ordenador_idordenador']
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
    atributos=AtributoSerialzier(many=True,read_only=True)

    class Meta:
        model=Equipo
        fields="__all__"
        depth=1

class OrdenadorNestedSerializer(serializers.ModelSerializer):
    perifericos=serializers.PrimaryKeyRelatedField(many=True,read_only=True)
    idordenador=EquipoSerializer()
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
    idotro_dispositivo=EquipoSerializer()
    class Meta:
        model=OtroDispositivo
        fields="__all__"
        depth=3
class OrdenadorHasLicenciaSerializer(serializers.ModelSerializer):
    class Meta:
        model=OrdenadorHasLicencia
        fields=['idordenador_has_licencia','llave','version','fecha_instalacion','licencia_idlicencia','ordenador_idordenador']
class TabletSerializer(serializers.ModelSerializer):
    class Meta:
        model=Tablet
        fields="__all__"