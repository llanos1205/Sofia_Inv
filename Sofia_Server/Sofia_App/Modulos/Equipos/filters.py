import rest_framework_filters as filters
import Sofia_Server.Sofia_App.Modulos.Equipos.models as models
class EquipoFilter(filters.FilterSet):
    class Meta:
        model=models.Equipo
        fields='__all__'
class OrdenadorFilter(filters.FilterSet):
    equipo=filters.RelatedFilter(EquipoFilter,field_name="idordenador",queryset=models.Equipo.objects.all())
    class Meta:
        model=models.Ordenador
        fields='__all__'