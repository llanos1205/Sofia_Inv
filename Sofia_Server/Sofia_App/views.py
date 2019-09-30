# from django.shortcuts import render
from django.contrib.auth.models import User, Group
from Sofia_Server.Sofia_App.models import (Equipo,Empresa,Area,Departamento,
                                            Regional,Ubicacion,Gerencia,Cargo,
                                            UsuarioAd,Cuenta,UsuarioCorreo,Equipo,
                                            Permiso,UsuarioAdHasPermiso,Ordenador,OtroDispositivo,
                                            Impresora,Licencia,Atributo,EquipoHasAtributo,Os,
                                            Auditoria,Asociacion,OrdenadorHasLicencia)
from Sofia_Server.Sofia_App.serializers import  (CuentaSerializer,GerenciaSerializer,UbicacionSerializer,
                                                RegionalSerializer,UserSerializer, GroupSerializer,EquipoSerializer,
                                                EmpresaSerializer,AreaSerializer,DepartamentoSerializer,CargoSerializer,
                                                UsuarioADSerializer,UsuarioCorreoSerializer,EquipoSerializer,
                                                PermisoSerializer,Permiso_UsuarioADSerializer,OrdenadorSerializer,
                                                OtroDispositivoSerializer,ImpresoraSerializer,LicenciaSerializer,
                                                AtributoSerialzier,EquipoHasAtributoSerializer,OsSerializer,
                                                AuditoriaSerializer,AsociacionSerializer,OrdenadorHasLicenciaSerializer)
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
    lookup_url_kwarg=['pk,pk2']
    def get_object(self):
        pk=self.kwargs['pk']
        pk2=self.kwargs['pk2']
        return UsuarioAdHasPermiso.objects.get(usuario_ad_idusuario_ad=pk,permiso_idpermiso=pk2)
    
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
    queryset=EquipoHasAtributo.objects.all()
    serializer_class=EquipoHasAtributoSerializer    
class Equipo_Atributo_Detail(generics.RetrieveUpdateDestroyAPIView):
    queryset=EquipoHasAtributo.objects.all()
    serializer_class=EquipoHasAtributoSerializer
    lookup_url_kwarg=['pk,pk2']
    def get_object(self):
        pk=self.kwargs['pk']
        pk2=self.kwargs['pk2']
        return EquipoHasAtributo.objects.get(equipo_idequipo=pk,atributo_idatributo=pk2)


class Os_List(generics.ListCreateAPIView):
    queryset=Os.objects.all()
    serializer_class=OsSerializer
class Os_Detail(generics.RetrieveUpdateDestroyAPIView):
    queryset=Os.objects.all()
    serializer_class=OsSerializer

class Auditoria_List(generics.ListCreateAPIView):
    queryset=Auditoria.objects.all()
    serializer_class=AuditoriaSerializer
class Auditoria_Detail(generics.RetrieveUpdateDestroyAPIView):
    queryset=Auditoria.objects.all()
    serializer_class=AuditoriaSerializer

class Asociacion_List(generics.ListCreateAPIView):
    queryset=Asociacion.objects.all()
    serializer_class=AsociacionSerializer
class Asociacion_Detail(generics.RetrieveUpdateDestroyAPIView):
    queryset=Asociacion.objects.all()
    serializer_class=AsociacionSerializer

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