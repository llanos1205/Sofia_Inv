
from rest_framework import viewsets,status,generics
from Sofia_Server.Sofia_App.Modulos.Transacciones.models import(
    Asociacion,Auditoria
)
from Sofia_Server.Sofia_App.Modulos.Transacciones.serializers import(
    AsociacionSerializer,AsociacionesNestedSerializer,AuditoriaSerializer
)
from rest_framework.renderers import AdminRenderer,JSONRenderer

from Sofia_Server.Sofia_App.Modulos.Transacciones import filters
class AsociacionNested_List(generics.ListAPIView):
    queryset=Asociacion.objects.all()
    serializer_class=AsociacionesNestedSerializer
    filter_class=filters.AsociacionFilter
class Auditoria_List(generics.ListCreateAPIView):
    queryset=Auditoria.objects.all()
    serializer_class=AuditoriaSerializer
    #renderer_classes = [AdminRenderer,JSONRenderer]
    filterset_fields = ('__all__')
class Auditoria_Detail(generics.RetrieveUpdateDestroyAPIView):
    queryset=Auditoria.objects.all()
    serializer_class=AuditoriaSerializer
class Asociacion_List(generics.ListCreateAPIView):
    queryset=Asociacion.objects.all()
    serializer_class=AsociacionSerializer
    filterset_fields = ('__all__')
class Asociacion_Detail(generics.RetrieveUpdateDestroyAPIView):
    queryset=Asociacion.objects.all()
    serializer_class=AsociacionSerializer

