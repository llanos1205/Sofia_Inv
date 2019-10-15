from Sofia_Server.Sofia_App.Modulos.Transacciones import models 
import rest_framework_filters as filters
from Sofia_Server.Sofia_App.Modulos.Equipos import filters as eqfilters
from Sofia_Server.Sofia_App.Modulos.Usuarios import filters as userfilters
class AsociacionFilter(filters.FilterSet):
    equipo=filters.RelatedFilter(eqfilters.EquipoFilter,related_name='equipo_idequipo',queryset=eqfilters.models.Equipo.objects.all())
    user=filters.RelatedFilter(userfilters.UsuarioADFilter,related_name='usuariofinal',queryset=userfilters.models.UsuarioAd.objects.all())
    class Meta:
        model=models.Asociacion
        fields="__all__"
