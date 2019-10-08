from Sofia_Server.Sofia_App.Modulos.InfoUser.models import Empresa,Cargo,Area,Gerencia,Ubicacion,Departamento,Permiso,Regional
from rest_framework import serializers
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
class PermisoSerializer(serializers.ModelSerializer):
    class Meta:
        model=Permiso
        fields=['idpermiso','nombre','estado']