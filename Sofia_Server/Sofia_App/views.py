# from django.shortcuts import render
from django.contrib.auth.models import User, Group
from Sofia_Server.Sofia_App.models import Equipo,Empresa
from rest_framework import viewsets,status,generics
from Sofia_Server.Sofia_App.serializers import UserSerializer, GroupSerializer,EquipoSerializer,EmpresaSerializer



class EmpresaList(generics.ListCreateAPIView):
    queryset=Empresa.objects.all()
    serializer_class=EmpresaSerializer
class Empresa_Detail(generics.RetrieveUpdateDestroyAPIView):
    queryset=Empresa.objects.all()
    serializer_class=EmpresaSerializer