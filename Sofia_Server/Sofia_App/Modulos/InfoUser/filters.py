import Sofia_Server.Sofia_App.Modulos.InfoUser.models as models
import rest_framework_filters as filters
class GerenciaFilter(filters.FilterSet):
    class Meta:
        model=models.Gerencia
        fields= {
             'nombre': ['exact', 'in', 'startswith','contains'],
             'descripcion': ['exact', 'in', 'startswith','contains'],
        }
class AreaFilter(filters.FilterSet):
    gerencia=filters.RelatedFilter(GerenciaFilter,field_name="gerencia_idgerencia",queryset=models.Gerencia.objects.all())
    class Meta:
        model=models.Area
        fields= {
             'nombre': ['exact', 'in', 'startswith','contains'],
             'descripcion': ['exact', 'in', 'startswith','contains'],
        }
class EmpresaFilter(filters.FilterSet):
    class Meta:
        model=models.Empresa
        fields= {
             'nombre': ['exact', 'in', 'startswith','contains'],
             'descripcion': ['exact', 'in', 'startswith','contains'],
        }

class RegionalFilter(filters.FilterSet):
    class Meta:
        model=models.Regional
        fields= {
             'nombre': ['exact', 'in', 'startswith','contains'],
        }
class UbicacionFilter(filters.FilterSet):
    class Meta:
        model=models.Ubicacion
        fields= {
             'direccion': ['exact', 'in', 'startswith','contains'],
             'edificio': ['exact', 'in', 'startswith','contains'],
        }
class CargoFilter(filters.FilterSet):
    class Meta:
        model=models.Cargo
        fields= {
             'nombre': ['exact', 'in', 'startswith','contains'],
             'descripcion': ['exact', 'in', 'startswith','contains'],
        }
class PermisoFilter(filters.FilterSet):
    class Meta:
        model=models.Permiso
        fields= {
             'nombre': ['exact', 'in', 'startswith','contains'],
        }