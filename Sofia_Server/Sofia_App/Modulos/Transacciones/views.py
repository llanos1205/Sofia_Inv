
from rest_framework import viewsets,status,generics,views
from Sofia_Server.Sofia_App.Modulos.Transacciones.models import(
    Asociacion,Auditoria
)
from Sofia_Server.Sofia_App.Modulos.Transacciones.serializers import(
    AsociacionSerializer,AsociacionesNestedSerializer,AuditoriaSerializer,AuditoriaNestedSerializer
)
from rest_framework.renderers import AdminRenderer,JSONRenderer

from Sofia_Server.Sofia_App.Modulos.Transacciones import filters

class AuditoriaNested_List(generics.ListAPIView):
    queryset=Auditoria.objects.all().order_by('pk')
    serializer_class=AuditoriaNestedSerializer
    filter_class=filters.AuditoriaFilter
class AsociacionNested_List(generics.ListAPIView):
    queryset=Asociacion.objects.all().order_by('pk')
    serializer_class=AsociacionesNestedSerializer
    filter_class=filters.AsociacionFilter
class Auditoria_List(generics.ListCreateAPIView):
    queryset=Auditoria.objects.all().order_by('pk')
    serializer_class=AuditoriaSerializer
    #renderer_classes = [AdminRenderer,JSONRenderer]
    filter_class=filters.AuditoriaFilter
class Auditoria_Detail(generics.RetrieveUpdateDestroyAPIView):
    queryset=Auditoria.objects.all()
    serializer_class=AuditoriaSerializer
class Asociacion_List(generics.ListCreateAPIView):
    queryset=Asociacion.objects.all().order_by('pk')
    serializer_class=AsociacionSerializer
    filterset_fields = ('__all__')
class Asociacion_Detail(generics.RetrieveUpdateDestroyAPIView):
    queryset=Asociacion.objects.all()
    serializer_class=AsociacionSerializer


