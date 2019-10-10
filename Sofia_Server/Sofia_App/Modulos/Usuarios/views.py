from rest_framework import viewsets,status,generics
from Sofia_Server.Sofia_App.Modulos.Usuarios.models import(
    UsuarioAd,UsuarioAdHasPermiso,Cuenta,UsuarioCorreo
)
from Sofia_Server.Sofia_App.Modulos.Usuarios.serializers import(
    CorreoNestedSerializer,UsuarioADSerializer,CuentaSerializer,
    UsuarioCorreoSerializer,UsuarioADSerializerFull,Permiso_UsuarioADSerializer
)
class CorreosNested_List(generics.ListAPIView):
    queryset=UsuarioCorreo.objects.all()
    serializer_class=CorreoNestedSerializer

class UsuarioAD_List(generics.ListCreateAPIView):
    queryset=UsuarioAd.objects.all()
    serializer_class=UsuarioADSerializer
    filterset_fields = ('area_idarea', 'ci')
class UsuarioAD_Nested_List(generics.ListAPIView):
    queryset=UsuarioAd.objects.all()
    serializer_class=UsuarioADSerializerFull
    

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
    