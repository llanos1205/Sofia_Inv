from Sofia_Server.Sofia_App.Modulos.Transacciones import models 
import rest_framework_filters as filters
from Sofia_Server.Sofia_App.Modulos.Equipos import filters as eqfilters
from Sofia_Server.Sofia_App.Modulos.Usuarios import filters as userfilters
class AsociacionFilter(filters.FilterSet):
    equipo=filters.RelatedFilter(eqfilters.EquipoFilter,field_name='equipo_idequipo',queryset=eqfilters.models.Equipo.objects.all())
    user=filters.RelatedFilter(userfilters.UsuarioADFilter,field_name='usuariofinal',queryset=userfilters.models.UsuarioAd.objects.all())
    cuenta=filters.RelatedFilter(userfilters.CuentaFilter,field_name='cuenta_idcuenta',queryset=userfilters.models.Cuenta.objects.all())
    class Meta:
        model=models.Asociacion
        fields = {
            'fecha_alta': ['exact', 'in', 'startswith','contains','gte'],
            'fecha_baja': ['exact', 'in', 'startswith','contains','lte'],
            'motivo': ['exact', 'in', 'startswith','contains'],
            'resposable': ['exact', 'in', 'startswith','contains'],
            }
class AuditoriaFilter(filters.FilterSet):
    user=filters.RelatedFilter(userfilters.CuentaFilter,field_name='usuario_ad_idusuario_ad',queryset=userfilters.models.Cuenta.objects.all())
    class Meta:
        model=models.Auditoria
        fields = {
            'fecha': ['exact', 'in', 'startswith','contains','gte'],
            'id_registro_afectado': ['exact', 'in', 'startswith','contains'],
            'tabla_afectada': ['exact', 'in', 'startswith','contains'],
            'accion': ['exact', 'in', 'startswith','contains'],
            'ip': ['exact', 'in', 'startswith','contains'],
            } 