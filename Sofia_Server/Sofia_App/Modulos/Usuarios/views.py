from rest_framework import viewsets,status,generics
from Sofia_Server.Sofia_App.Modulos.Usuarios.models import(
    UsuarioAd,UsuarioAdHasPermiso,Cuenta,UsuarioCorreo
)
from Sofia_Server.Sofia_App.Modulos.Usuarios.serializers import(
    CorreoNestedSerializer,UsuarioADSerializer,CuentaSerializer,
    UsuarioCorreoSerializer,UsuarioADSerializerFull,Permiso_UsuarioADSerializer
)
from rest_framework.renderers import AdminRenderer
from ..Usuarios import filters
class CorreosNested_List(generics.ListAPIView):
    queryset=UsuarioCorreo.objects.all().order_by("pk")
    serializer_class=CorreoNestedSerializer
    filter_class=filters.CorreoFilter
class UsuarioAD_List(generics.ListCreateAPIView):
    queryset=UsuarioAd.objects.all().order_by('pk')
    serializer_class=UsuarioADSerializer
    filter_class=filters.UsuarioADFilter
class UsuarioAD_Nested_List(generics.ListAPIView):
    queryset=UsuarioAd.objects.all().order_by("pk")
    serializer_class=UsuarioADSerializerFull
    filter_class=filters.UsuarioADFilter
class UsuarioAD_Detail(generics.RetrieveUpdateDestroyAPIView):
    queryset=UsuarioAd.objects.all()
    serializer_class=UsuarioADSerializer
    
class Cuenta_List(generics.ListCreateAPIView):
    queryset=Cuenta.objects.all().order_by("pk")
    serializer_class=CuentaSerializer
    filter_class=filters.CuentaFilter
class Cuenta_Detail(generics.RetrieveUpdateDestroyAPIView):
    queryset=Cuenta.objects.all()
    serializer_class=CuentaSerializer

class UsuarioCorreo_List(generics.ListCreateAPIView):
    queryset=UsuarioCorreo.objects.all().order_by("pk")
    serializer_class=UsuarioCorreoSerializer
    filter_class=filters.CorreoFilter
class UsuarioCorreo_Detail(generics.RetrieveUpdateDestroyAPIView):
    queryset=UsuarioCorreo.objects.all()
    serializer_class=UsuarioCorreoSerializer
class Usuario_Permiso_List(generics.ListCreateAPIView):
    queryset=UsuarioAdHasPermiso.objects.all().order_by("pk")
    serializer_class=Permiso_UsuarioADSerializer
    filterset_fields = ('__all__')
    
class Usuario_Permiso_Detail(generics.RetrieveUpdateDestroyAPIView):
    queryset=UsuarioAdHasPermiso.objects.all()
    serializer_class=Permiso_UsuarioADSerializer
    lookup_url_kwarg=['pk,pk2']
    def get_object(self):
        pk=self.kwargs['pk']
        pk2=self.kwargs['pk2']
        return UsuarioAdHasPermiso.objects.get(usuario_ad_idusuario_ad=pk,permiso_idpermiso=pk2)

# #ejemplo de front end web basico"
#NOTA debe existir un .html con el nombre de la funcion dentro de la carpeta templates
# from django.http import HttpResponse
# from django.template import loader

# from .models import Question


# def index(request):
#     latest_question_list = Question.objects.order_by('-pub_date')[:5]
#     template = loader.get_template('polls/index.html')
#     context = {
#         'latest_question_list': latest_question_list,
#     }
#     return HttpResponse(template.render(context, request))