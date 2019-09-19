# from django.shortcuts import render
from django.contrib.auth.models import User, Group
from Sofia_Server.Sofia_App.models import Equipo,Empresa,Area,Departamento,Regional,Ubicacion,Gerencia
from Sofia_Server.Sofia_App.serializers import  GerenciaSerializer,UbicacionSerializer,RegionalSerializer,UserSerializer, GroupSerializer,EquipoSerializer,EmpresaSerializer,AreaSerializer,DepartamentoSerializer
from rest_framework import viewsets,status,generics



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
