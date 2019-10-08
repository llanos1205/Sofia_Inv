from rest_framework import viewsets,status,generics
from Sofia_Server.Sofia_App.Modulos.Equipos.models import (
    Equipo,Ordenador,Impresora,OtroDispositivo,
    OtroDispositivoHasAtributo,Os,OrdenadorHasLicencia,Licencia,Atributo,Tablet
)
from Sofia_Server.Sofia_App.Modulos.Equipos.serializers import (
    OrdenadorHasLicenciaSerializer,OsSerializer,
    EquipoNestedSerializer,OrdenadorNestedSerializer,ImpresoraNestedSerializer,
    OtrosDispositivosNestedSerializer,EquipoSerializer,OrdenadorSerializer,
    LicenciaSerializer,AtributoSerialzier,OtroDispositivoSerializer,
    ImpresoraSerializer,OtroDispositivoHasAtributoSerializer,TabletSerializer

)
class OrdenadorNested_List(generics.ListAPIView):
    queryset=Ordenador.objects.all()
    serializer_class=OrdenadorNestedSerializer
class ImpresoraNested_List(generics.ListAPIView):
    queryset=Impresora.objects.all()
    serializer_class=ImpresoraNestedSerializer
class OtroDispositivosNested_List(generics.ListAPIView):
    queryset=OtroDispositivo.objects.all()
    serializer_class=OtrosDispositivosNestedSerializer   

class EquipoNested_List(generics.ListAPIView):
    queryset=Equipo.objects.all()
    serializer_class=EquipoNestedSerializer  
class Equipo_List(generics.ListCreateAPIView):
    queryset=Equipo.objects.all()
    serializer_class=EquipoSerializer
class Equipo_Detail(generics.RetrieveUpdateDestroyAPIView):
    queryset=Equipo.objects.all()
    serializer_class=EquipoSerializer




class Equio_List(generics.ListCreateAPIView):
    queryset=Equipo.objects.all()
    serializer_class=EquipoSerializer
class Equio_List(generics.RetrieveUpdateDestroyAPIView):
    queryset=Equipo.objects.all()
    serializer_class=EquipoSerializer

class Ordenador_List(generics.ListCreateAPIView):
    queryset=Ordenador.objects.all()
    
    serializer_class=OrdenadorSerializer
class Ordenador_Detail(generics.RetrieveUpdateDestroyAPIView):
    queryset=Ordenador.objects.all()
    serializer_class=OrdenadorSerializer

class OtroDispositivo_List(generics.ListCreateAPIView):
    queryset=OtroDispositivo.objects.all()
    serializer_class=OtroDispositivoSerializer
class OtroDispositivo_Detail(generics.RetrieveUpdateDestroyAPIView):
    queryset=OtroDispositivo.objects.all()
    serializer_class=OtroDispositivoSerializer

class Impresora_List(generics.ListCreateAPIView):
    queryset=Impresora.objects.all()
    serializer_class=ImpresoraSerializer
class Impresora_Detail(generics.RetrieveUpdateDestroyAPIView):
    queryset=Impresora.objects.all()
    serializer_class=ImpresoraSerializer

class Licencia_List(generics.ListCreateAPIView):
    queryset=Licencia.objects.all()
    serializer_class=LicenciaSerializer
class Licencia_Detail(generics.RetrieveUpdateDestroyAPIView):
    queryset=Licencia.objects.all()
    serializer_class=LicenciaSerializer

class Atributo_List(generics.ListCreateAPIView):
    queryset=Atributo.objects.all()
    serializer_class=AtributoSerialzier
class Atributo_Detail(generics.RetrieveUpdateDestroyAPIView):
    queryset=Atributo.objects.all()
    serializer_class=AtributoSerialzier

class Equipo_Atributo_List(generics.ListCreateAPIView):
    queryset=OtroDispositivoHasAtributo.objects.all()
    serializer_class=OtroDispositivoHasAtributoSerializer
class Equipo_Atributo_Detail(generics.RetrieveUpdateDestroyAPIView):
    queryset=OtroDispositivoHasAtributo.objects.all()
    serializer_class=OtroDispositivoHasAtributoSerializer
    lookup_url_kwarg=['pk,pk2']
    def get_object(self):
        pk=self.kwargs['pk']
        pk2=self.kwargs['pk2']
        return OtroDispositivoHasAtributo.objects.get(otro_dispositivo_idotro_dispositivo=pk,atributo_idatributo=pk2)


class Os_List(generics.ListCreateAPIView):
    queryset=Os.objects.all()
    serializer_class=OsSerializer
class Os_Detail(generics.RetrieveUpdateDestroyAPIView):
    queryset=Os.objects.all()
    serializer_class=OsSerializer

class OrdenadorHasLicencia_List(generics.ListCreateAPIView):
    queryset=OrdenadorHasLicencia.objects.all()
    serializer_class=OrdenadorHasLicenciaSerializer
class OrdenadorHasLicencia_Detail(generics.RetrieveUpdateDestroyAPIView):
    queryset=OrdenadorHasLicencia.objects.all()
    serializer_class=OrdenadorHasLicenciaSerializer
    lookup_url_kwarg=['pk2,pk3']
    def get_object(self):
        pk2=self.kwargs['pk2']
        pk3=self.kwargs['pk3']
        return OrdenadorHasLicencia.objects.get(ordenador_idordenador=pk2,licencia_idlicencia=pk3)

class Tablet_List(generics.ListCreateAPIView):
    queryset=Tablet.objects.all().order_by("imei")
    serializer_class=TabletSerializer