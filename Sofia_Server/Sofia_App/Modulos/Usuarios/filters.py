import rest_framework_filters as filters
import Sofia_Server.Sofia_App.Modulos.Usuarios.models as models
import Sofia_Server.Sofia_App.Modulos.InfoUser.filters as infofilters
class CuentaFilter(filters.FilterSet):
    class Meta:
        model=models.Cuenta
        fields="__all__"

class UsuarioADFilter(filters.FilterSet):
    area=filters.RelatedFilter(infofilters.AreaFilter,field_name="area_idarea",queryset=infofilters.models.Area.objects.all())
    empresa=filters.RelatedFilter(infofilters.EmpresaFilter,field_name="empresa_idempresa",queryset=infofilters.models.Empresa.objects.all())
    gerencia=filters.RelatedFilter(infofilters.GerenciaFilter,field_name="gerencia_idgerencia",queryset=infofilters.models.Gerencia.objects.all())
    regional=filters.RelatedFilter(infofilters.RegionalFilter,field_name="regional_idregional",queryset=infofilters.models.Regional.objects.all())
    ubicacion=filters.RelatedFilter(infofilters.UbicacionFilter,field_name="ubicacion_idubicacion",queryset=infofilters.models.Ubicacion.objects.all())
    cuenta=filters.RelatedFilter(CuentaFilter, field_name="cuenta_idcuenta", queryset=models.Cuenta.objects.all())
    cargo=filters.RelatedFilter(infofilters.GerenciaFilter,field_name="gerencia_idgerencia",queryset=infofilters.models.Gerencia.objects.all())
    permiso=filters.RelatedFilter(infofilters.GerenciaFilter,field_name="gerencia_idgerencia",queryset=infofilters.models.Gerencia.objects.all())
  
    class Meta:
        model=models.UsuarioAd
        fields="__all__"