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
    filterset_fields = ('__all__')
class Empresa_Detail(generics.RetrieveUpdateDestroyAPIView):
    queryset=Empresa.objects.all()
    serializer_class=EmpresaSerializer

class Departamento_List(generics.ListCreateAPIView):
    queryset=Departamento.objects.all()
    serializer_class=DepartamentoSerializer
    filterset_fields = ('__all__')
class Departamento_Detail(generics.RetrieveUpdateDestroyAPIView):
    queryset=Departamento.objects.all()
    serializer_class=DepartamentoSerializer

class Area_List(generics.ListCreateAPIView):
    queryset=Area.objects.all()
    serializer_class=AreaSerializer
    filterset_fields = ('__all__')
class Area_Detail(generics.RetrieveUpdateDestroyAPIView):
    queryset=Area.objects.all()
    serializer_class=AreaSerializer

class Gerencia_List(generics.ListCreateAPIView):
    queryset=Gerencia.objects.all()
    serializer_class=GerenciaSerializer
    filterset_fields = ('__all__')
class Gerencia_Detail(generics.RetrieveUpdateDestroyAPIView):
    queryset=Gerencia.objects.all()
    serializer_class=GerenciaSerializer

class Regional_List(generics.ListCreateAPIView):
    queryset=Regional.objects.all()
    serializer_class=RegionalSerializer
    filterset_fields = ('__all__')
class Regional_Detail(generics.RetrieveUpdateDestroyAPIView):
    queryset=Regional.objects.all()
    serializer_class=RegionalSerializer

class Ubicacion_List(generics.ListCreateAPIView):
    queryset=Ubicacion.objects.all()
    serializer_class=UbicacionSerializer
    filterset_fields = ('__all__')
class Ubicacion_Detail(generics.RetrieveUpdateDestroyAPIView):
    queryset=Ubicacion.objects.all()
    serializer_class=UbicacionSerializer

class Cargo_List(generics.ListCreateAPIView):
    queryset=Cargo.objects.all()
    serializer_class=CargoSerializer
    filterset_fields = ('__all__')
class Cargo_Detail(generics.RetrieveUpdateDestroyAPIView):
    queryset=Cargo.objects.all()
    serializer_class=CargoSerializer  
class Permiso_List(generics.ListCreateAPIView):
    queryset=Permiso.objects.all()
    serializer_class=PermisoSerializer
    filterset_fields = ('__all__')
class Permiso_Detail(generics.RetrieveUpdateDestroyAPIView):
    queryset=Permiso.objects.all()
    serializer_class=PermisoSerializer