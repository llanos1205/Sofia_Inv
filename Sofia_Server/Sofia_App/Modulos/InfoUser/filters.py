import Sofia_Server.Sofia_App.Modulos.InfoUser.models as models
import rest_framework_filters as filters

class DepartamentoFilter(filters.FilterSet):
    class Meta:
        model=models.Departamento
        fields="__all__"
class AreaFilter(filters.FilterSet):
    departamento=filters.RelatedFilter(DepartamentoFilter,field_name="departamento_iddepartamento",queryset=models.Departamento.objects.all())
    class Meta:
        model=models.Area
        fields="__all__"
class EmpresaFilter(filters.FilterSet):
    class Meta:
        model=models.Empresa
        fields="__all__"
class GerenciaFilter(filters.FilterSet):
    class Meta:
        model=models.Gerencia
        fields="__all__"
class RegionalFilter(filters.FilterSet):
    class Meta:
        model=models.Regional
        fields="__all__"
class UbicacionFilter(filters.FilterSet):
    class Meta:
        model=models.Ubicacion
        fields="__all__"
class CargoFilter(filters.FilterSet):
    class Meta:
        model=models.Cargo
        fields="__all__"
class PermisoFilter(filters.FilterSet):
    class Meta:
        model=models.Permiso
        fields="__all__"