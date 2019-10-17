import rest_framework_filters as filters
import Sofia_Server.Sofia_App.Modulos.Equipos.models as models
import Sofia_Server.Sofia_App.Modulos.Usuarios.filters as UserFilters
class OsFilter(filters.FilterSet):
    class Meta:
        model=models.Os
        fields="__all__"
class LicenciaFilter(filters.FilterSet):
    class Meta:
        model=models.Licencia
        fields="__all__"
class EquipoFilter(filters.FilterSet):
    usuario=filters.RelatedFilter(UserFilters.UsuarioADFilter,field_name="usuarios",queryset=UserFilters.models.UsuarioAd.objects.all())
    class Meta:
        model=models.Equipo
        fields='__all__'
class AtributoFilter(filters.FilterSet):
    class Meta:
        model=models.Atributo
        fields="__all__"
class OrdenadorFilter(filters.FilterSet):
    equipo=filters.RelatedFilter(EquipoFilter ,field_name="idordenador",queryset=models.Equipo.objects.all())
    Oss=filters.RelatedFilter(OsFilter ,field_name="os_idos",queryset=models.Os.objects.all())
    class Meta:
        model=models.Ordenador
        fields='__all__'
class ImpresoraFilter(filters.FilterSet):
    equipo=filters.RelatedFilter(EquipoFilter ,field_name="idimpresora",queryset=models.Equipo.objects.all())
    class Meta:
        model=models.Impresora
        fields="__all__"
        depth=2

class OtroDispositivoFilter(filters.FilterSet):
    equipo=filters.RelatedFilter(EquipoFilter ,field_name="idotro_dispositivo",queryset=models.Equipo.objects.all())
    atributos=filters.RelatedFilter(AtributoFilter ,field_name="atributos",queryset=models.Atributo.objects.all())
    class Meta:
        model=models.OtroDispositivo
        fields="__all__"
class OrdenadorHasLicenciaFilter(filters.FilterSet):
    equipo=filters.RelatedFilter(OrdenadorFilter ,field_name="ordenador_idordenador",queryset=models.Ordenador.objects.all())
    licencia=filters.RelatedFilter(LicenciaFilter,field_name="licencia_idlicencia",queryset=models.Licencia.objects.all())
    class Meta:
        model=models.OrdenadorHasLicencia
        fields="__all__"