import rest_framework_filters as filters
import Sofia_Server.Sofia_App.Modulos.Equipos.models as models
import Sofia_Server.Sofia_App.Modulos.Usuarios.filters as UserFilters
class OsFilter(filters.FilterSet):
    class Meta:
        model=models.Os
        fields = {
            'nombre': ['exact', 'in', 'startswith','contains'],
            'servicio': ['exact', 'in', 'startswith','contains'],
            'arquitectura': ['exact', 'in', 'startswith','contains'],
            }
class LicenciaFilter(filters.FilterSet):
    class Meta:
        model=models.Licencia
        fields = {
            'producto': ['exact', 'in', 'startswith','contains'],
           }
class EquipoFilter(filters.FilterSet):
    usuario=filters.RelatedFilter(UserFilters.UsuarioADFilter,field_name="usuarios",queryset=UserFilters.models.UsuarioAd.objects.all())
    class Meta:
        model=models.Equipo
        fields = {
            'marca': ['exact', 'in', 'startswith','contains'],
            'modelo': ['exact', 'in', 'startswith','contains'],
            'nro_serie': ['exact', 'in', 'startswith','contains'],
            'nro_activo_fijo': ['exact', 'in', 'startswith','contains'],
            'ip': ['exact', 'in', 'startswith','contains'],
           }
class AtributoFilter(filters.FilterSet):
    class Meta:
        model=models.Atributo
        fields = {
            'nombre': ['exact', 'in', 'startswith','contains'],
        }
class OrdenadorFilter(filters.FilterSet):
    equipo=filters.RelatedFilter(EquipoFilter ,field_name="idordenador",queryset=models.Equipo.objects.all())
    Oss=filters.RelatedFilter(OsFilter ,field_name="os_idos",queryset=models.Os.objects.all())
    class Meta:
        model=models.Ordenador
        fields = {            
            'marca': ['exact', 'in', 'startswith','contains'],
            'modelo': ['exact', 'in', 'startswith','contains'],
            'nro_serie': ['exact', 'in', 'startswith','contains'],
            'nro_activo_fijo': ['exact', 'in', 'startswith','contains'],
            'ip': ['exact', 'in', 'startswith','contains'],
            'tipo': ['exact', 'in', 'startswith','contains'],
            'mac': ['exact', 'in', 'startswith','contains'],
            'hostname': ['exact', 'in', 'startswith','contains'],
            'procesador': ['exact', 'in', 'startswith','contains'],
            'ram': ['exact', 'in', 'startswith','contains'],
            'almacenamiento': ['exact', 'in', 'startswith','contains'],
            'tipo_almacenamiento': ['exact', 'in', 'startswith','contains'],
        }
class ImpresoraFilter(filters.FilterSet):
    equipo=filters.RelatedFilter(EquipoFilter ,field_name="idimpresora",queryset=models.Equipo.objects.all())
    class Meta:
        model=models.Impresora
        fields = {
            'marca': ['exact', 'in', 'startswith','contains'],
            'modelo': ['exact', 'in', 'startswith','contains'],
            'nro_serie': ['exact', 'in', 'startswith','contains'],
            'nro_activo_fijo': ['exact', 'in', 'startswith','contains'],
            'ip': ['exact', 'in', 'startswith','contains'],
            'tipo': ['exact', 'in', 'startswith','contains'],
            'tinta': ['exact', 'in', 'startswith','contains'],
        }
        depth=2
class OtroDispositivoFilter(filters.FilterSet):
    equipo=filters.RelatedFilter(EquipoFilter ,field_name="idotro_dispositivo",queryset=models.Equipo.objects.all())
    atributos=filters.RelatedFilter(AtributoFilter ,field_name="atributos",queryset=models.Atributo.objects.all())
    class Meta:
        model=models.OtroDispositivo
        fields = {
            'marca': ['exact', 'in', 'startswith','contains'],
            'modelo': ['exact', 'in', 'startswith','contains'],
            'nro_serie': ['exact', 'in', 'startswith','contains'],
            'nro_activo_fijo': ['exact', 'in', 'startswith','contains'],
            'ip': ['exact', 'in', 'startswith','contains'],
            'nombre': ['exact', 'in', 'startswith','contains'],
        }
class OrdenadorHasLicenciaFilter(filters.FilterSet):
    equipo=filters.RelatedFilter(OrdenadorFilter ,field_name="ordenador_idordenador",queryset=models.Ordenador.objects.all())
    licencia=filters.RelatedFilter(LicenciaFilter,field_name="licencia_idlicencia",queryset=models.Licencia.objects.all())
    class Meta:
        model=models.OrdenadorHasLicencia
        fields = {
            'llave': ['exact', 'in', 'startswith','contains'],
            'version': ['exact', 'in', 'startswith','contains'],
            'fecha_instalacion': ['exact', 'in', 'startswith','contains','gte'],
        }