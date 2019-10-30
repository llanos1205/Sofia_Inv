import rest_framework_filters as filters
import Sofia_Server.Sofia_App.Modulos.Usuarios.models as models
import Sofia_Server.Sofia_App.Modulos.InfoUser.filters as infofilters
from rest_framework import viewsets
class CuentaFilter(filters.FilterSet):
    user=filters.RelatedFilter('UsuarioADFilter',field_name="Usuarios",queryset=models.UsuarioAd.objects.all())
    class Meta:
        model=models.Cuenta
        fields= {
            'idcuenta': ['exact', 'in', 'startswith','contains'],
             'usuario': ['exact', 'in', 'startswith','contains'],
             'contrasena': ['exact', 'in', 'startswith','contains'],
        }

class UsuarioADFilter(filters.FilterSet):
    area=filters.RelatedFilter(infofilters.AreaFilter,field_name="area_idarea",queryset=infofilters.models.Area.objects.all())
    empresa=filters.RelatedFilter(infofilters.EmpresaFilter,field_name="empresa_idempresa",queryset=infofilters.models.Empresa.objects.all())
    gerencia=filters.RelatedFilter(infofilters.GerenciaFilter,field_name="gerencia_idgerencia",queryset=infofilters.models.Gerencia.objects.all())
    regional=filters.RelatedFilter(infofilters.RegionalFilter,field_name="regional_idregional",queryset=infofilters.models.Regional.objects.all())
    ubicacion=filters.RelatedFilter(infofilters.UbicacionFilter,field_name="ubicacion_idubicacion",queryset=infofilters.models.Ubicacion.objects.all())
    cuenta=filters.RelatedFilter(CuentaFilter, field_name="cuenta_idcuenta", queryset=models.Cuenta.objects.all())
    cargo=filters.RelatedFilter(infofilters.CargoFilter,field_name="cargo_idcargo",queryset=infofilters.models.Cargo.objects.all())
    permiso=filters.RelatedFilter(infofilters.PermisoFilter,field_name="permisos",queryset=infofilters.models.Permiso.objects.all())
    
    class Meta:
        model=models.UsuarioAd
        fields= {
             'nombre': ['exact', 'in', 'startswith','contains'],
             'apellido': ['exact', 'in', 'startswith','contains'],
             'ci': ['exact', 'in', 'startswith','contains'],
        }
       
class CorreoFilter(filters.FilterSet):
    user=filters.RelatedFilter(UsuarioADFilter,field_name="usuario_ad_idusuario_ad1",queryset=models.UsuarioAd.objects.all())
    class Meta:
        model=models.UsuarioCorreo
        fields= {
             'correo': ['exact', 'in', 'startswith','contains'],
             'contrasena': ['exact', 'in', 'startswith','contains'],
             'tipo': ['exact', 'in', 'startswith','contains'],
        }