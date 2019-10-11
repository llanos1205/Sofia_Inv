import rest_framework_filters as filters
import Sofia_Server.Sofia_App.Modulos.Usuarios.models as models

class UsuarioADFilter(filters.FilterSet):
    class Meta:
        model=models.UsuarioAd
        fields="__all__"