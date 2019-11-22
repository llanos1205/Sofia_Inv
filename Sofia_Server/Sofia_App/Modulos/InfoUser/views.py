from rest_framework import viewsets,status,generics
from Sofia_Server.Sofia_App.Modulos.InfoUser.serializers import (
    EmpresaSerializer,AreaSerializer,GerenciaSerializer,
    RegionalSerializer,UbicacionSerializer,CargoSerializer,PermisoSerializer,AreaNestedSerializer
)
from Sofia_Server.Sofia_App.Modulos.InfoUser.models import (
    Empresa,Gerencia,Cargo,Ubicacion,
    Regional,Area,Permiso
)
from Sofia_Server.Sofia_App.Modulos.InfoUser import filters
class EmpresaList(generics.ListCreateAPIView):
    queryset=Empresa.objects.all().order_by("pk")
    serializer_class=EmpresaSerializer
    filter_class=filters.EmpresaFilter
class Empresa_Detail(generics.RetrieveUpdateDestroyAPIView):
    queryset=Empresa.objects.all()
    serializer_class=EmpresaSerializer

class Area_List(generics.ListCreateAPIView):
    queryset=Area.objects.all().order_by("pk")
    serializer_class=AreaSerializer
    filter_class=filters.AreaFilter
class AreaNested_List(generics.ListCreateAPIView):
    queryset=Area.objects.all().order_by("pk")
    serializer_class=AreaNestedSerializer
    filter_class=filters.AreaFilter
class Area_Detail(generics.RetrieveUpdateDestroyAPIView):
    queryset=Area.objects.all()
    serializer_class=AreaSerializer

class Gerencia_List(generics.ListCreateAPIView):
    queryset=Gerencia.objects.all().order_by("pk")
    serializer_class=GerenciaSerializer
    filter_class=filters.GerenciaFilter
class Gerencia_Detail(generics.RetrieveUpdateDestroyAPIView):
    queryset=Gerencia.objects.all()
    serializer_class=GerenciaSerializer

class Regional_List(generics.ListCreateAPIView):
    queryset=Regional.objects.all().order_by("pk")
    serializer_class=RegionalSerializer
    filter_class=filters.RegionalFilter
class Regional_Detail(generics.RetrieveUpdateDestroyAPIView):
    queryset=Regional.objects.all()
    serializer_class=RegionalSerializer

class Ubicacion_List(generics.ListCreateAPIView):
    queryset=Ubicacion.objects.all().order_by("pk")
    serializer_class=UbicacionSerializer
    filter_class=filters.UbicacionFilter
class Ubicacion_Detail(generics.RetrieveUpdateDestroyAPIView):
    queryset=Ubicacion.objects.all()
    serializer_class=UbicacionSerializer

class Cargo_List(generics.ListCreateAPIView):
    queryset=Cargo.objects.all().order_by("pk")
    serializer_class=CargoSerializer
    filter_class=filters.CargoFilter
class Cargo_Detail(generics.RetrieveUpdateDestroyAPIView):
    queryset=Cargo.objects.all()
    serializer_class=CargoSerializer  
class Permiso_List(generics.ListCreateAPIView):
    queryset=Permiso.objects.all().order_by("pk")
    serializer_class=PermisoSerializer
    filter_class=filters.PermisoFilter
class Permiso_Detail(generics.RetrieveUpdateDestroyAPIView):
    queryset=Permiso.objects.all()
    serializer_class=PermisoSerializer

