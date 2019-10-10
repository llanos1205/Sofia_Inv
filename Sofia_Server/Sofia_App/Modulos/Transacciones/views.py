
from rest_framework import viewsets,status,generics
from Sofia_Server.Sofia_App.Modulos.Transacciones.models import(
    Asociacion,Auditoria
)
from Sofia_Server.Sofia_App.Modulos.Transacciones.serializers import(
    AsociacionSerializer,AsociacionesNestedSerializer,AuditoriaSerializer
)
class AsociacionNested_List(generics.ListAPIView):
    queryset=Asociacion.objects.all()
    serializer_class=AsociacionesNestedSerializer
    filterset_fields = ('__all__')
class Auditoria_List(generics.ListCreateAPIView):
    queryset=Auditoria.objects.all()
    serializer_class=AuditoriaSerializer
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

