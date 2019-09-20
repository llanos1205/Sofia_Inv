# from django.shortcuts import render
from django.contrib.auth.models import User, Group
from Sofia_Server.Sofia_App.models import (Equipo,Empresa,Area,Departamento,
                                            Regional,Ubicacion,Gerencia,Cargo,
                                            UsuarioAd,Cuenta,UsuarioCorreo,Equipo,
                                            Permiso,UsuarioAdHasPermiso,Ordenador,OtroDispositivo,
                                            Impresora,Licencia,Atributo)
from Sofia_Server.Sofia_App.serializers import  (CuentaSerializer,GerenciaSerializer,UbicacionSerializer,
                                                RegionalSerializer,UserSerializer, GroupSerializer,EquipoSerializer,
                                                EmpresaSerializer,AreaSerializer,DepartamentoSerializer,CargoSerializer,
                                                UsuarioADSerializer,UsuarioCorreoSerializer,EquipoSerializer,
                                                PermisoSerializer,Permiso_UsuarioADSerializer,OrdenadorSerializer,
                                                OtroDispositivoSerializer,ImpresoraSerializer,LicenciaSerializer,
                                                AtributoSerialzier)
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

class Cargo_List(generics.ListCreateAPIView):
    queryset=Cargo.objects.all()
    serializer_class=CargoSerializer
class Cargo_Detail(generics.RetrieveDestroyAPIView):
    queryset=Cargo.objects.all()
    serializer_class=CargoSerializer  

class UsuarioAD_List(generics.ListCreateAPIView):
    queryset=UsuarioAd.objects.all()
    serializer_class=UsuarioADSerializer
class UsuarioAD_Detail(generics.RetrieveUpdateDestroyAPIView):
    queryset=UsuarioAd.objects.all()
    serializer_class=UsuarioADSerializer

class Cuenta_List(generics.ListCreateAPIView):
    queryset=Cuenta.objects.all()
    serializer_class=CuentaSerializer
class Cuenta_Detail(generics.RetrieveUpdateDestroyAPIView):
    queryset=Cuenta.objects.all()
    serializer_class=CuentaSerializer

class UsuarioCorreo_List(generics.ListCreateAPIView):
    queryset=UsuarioCorreo.objects.all()
    serializer_class=UsuarioCorreoSerializer
class UsuarioCorreo_Detail(generics.RetrieveUpdateDestroyAPIView):
    queryset=UsuarioCorreo.objects.all()
    serializer_class=UsuarioCorreoSerializer

class Equipo_List(generics.ListCreateAPIView):
    queryset=Equipo.objects.all()
    serializer_class=EquipoSerializer
class Equipo_Detail(generics.RetrieveUpdateDestroyAPIView):
    queryset=Equipo.objects.all()
    serializer_class=EquipoSerializer

class Permiso_List(generics.ListCreateAPIView):
    queryset=Permiso.objects.all()
    serializer_class=PermisoSerializer
class Permiso_Detail(generics.RetrieveUpdateDestroyAPIView):
    queryset=Permiso.objects.all()
    serializer_class=PermisoSerializer

class Usuario_Permiso_List(generics.ListCreateAPIView):
    queryset=UsuarioAdHasPermiso.objects.all()
    serializer_class=Permiso_UsuarioADSerializer
class Usuario_Permiso_Detail(generics.RetrieveUpdateDestroyAPIView):
    queryset=UsuarioAdHasPermiso.objects.all()
    serializer_class=Permiso_UsuarioADSerializer

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
