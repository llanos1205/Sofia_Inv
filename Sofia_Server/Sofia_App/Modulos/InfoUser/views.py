from rest_framework import viewsets,status,generics
from Sofia_Server.Sofia_App.Modulos.InfoUser.serializers import (
    EmpresaSerializer,DepartamentoSerializer,AreaSerializer,GerenciaSerializer,
    RegionalSerializer,UbicacionSerializer,CargoSerializer,PermisoSerializer
)
from Sofia_Server.Sofia_App.Modulos.InfoUser.models import (
    Empresa,Departamento,Gerencia,Cargo,Ubicacion,
    Regional,Area,Permiso
)

class EmpresaList(generics.ListCreateAPIView):
    queryset=Empresa.objects.all()
    serializer_class=EmpresaSerializer
class Empresa_Detail(generics.RetrieveUpdateDestroyAPIView):
    queryset=Empresa.objects.all()
    serializer_class=EmpresaSerializer

class Departamento_List(generics.ListCreateAPIView):
    queryset=Departamento.objects.all()
    serializer_class=DepartamentoSerializer
class Departamento_Detail(generics.RetrieveUpdateDestroyAPIView):
    queryset=Departamento.objects.all()
    serializer_class=DepartamentoSerializer

class Area_List(generics.ListCreateAPIView):
    queryset=Area.objects.all()
    serializer_class=AreaSerializer
class Area_Detail(generics.RetrieveUpdateDestroyAPIView):
    queryset=Area.objects.all()
    serializer_class=AreaSerializer

class Gerencia_List(generics.ListCreateAPIView):
    queryset=Gerencia.objects.all()
    serializer_class=GerenciaSerializer
class Gerencia_Detail(generics.RetrieveUpdateDestroyAPIView):
    queryset=Gerencia.objects.all()
    serializer_class=GerenciaSerializer

class Regional_List(generics.ListCreateAPIView):
    queryset=Regional.objects.all()
    serializer_class=RegionalSerializer
class Regional_Detail(generics.RetrieveUpdateDestroyAPIView):
    queryset=Regional.objects.all()
    serializer_class=RegionalSerializer

class Ubicacion_List(generics.ListCreateAPIView):
    queryset=Ubicacion.objects.all()
    serializer_class=UbicacionSerializer
class Ubicacion_Detail(generics.RetrieveUpdateDestroyAPIView):
    queryset=Ubicacion.objects.all()
    serializer_class=UbicacionSerializer

class Cargo_List(generics.ListCreateAPIView):
    queryset=Cargo.objects.all()
    serializer_class=CargoSerializer
class Cargo_Detail(generics.RetrieveUpdateDestroyAPIView):
    queryset=Cargo.objects.all()
    serializer_class=CargoSerializer  
class Permiso_List(generics.ListCreateAPIView):
    queryset=Permiso.objects.all()
    serializer_class=PermisoSerializer
class Permiso_Detail(generics.RetrieveUpdateDestroyAPIView):
    queryset=Permiso.objects.all()
    serializer_class=PermisoSerializer