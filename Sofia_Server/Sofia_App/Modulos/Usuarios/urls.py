 
from django.urls import path
from Sofia_Server.Sofia_App.Modulos.Usuarios import views
from rest_framework.urlpatterns import format_suffix_patterns
urlpatterns = [
    path('UsuariosAD/',views.UsuarioAD_List.as_view()),
    path('UsuariosAD/Nested/',views.UsuarioAD_Nested_List.as_view()),
    path('UsuariosAD/<int:pk>/',views.UsuarioAD_Detail.as_view()),

    path('Cuentas/',views.Cuenta_List.as_view()),
    path('Cuentas/<int:pk>/',views.Cuenta_Detail.as_view()),
    path('Usuario_Permisos/',views.Usuario_Permiso_List.as_view()),
    path('Usuario_Permisos/<int:pk>/<int:pk2>/',views.Usuario_Permiso_Detail.as_view()),

    path('UsuarioCorreos/',views.UsuarioCorreo_List.as_view()),
    path('UsuarioCorreos/<int:pk>/',views.UsuarioCorreo_Detail.as_view()),
    path('UsuarioCorreos/Nested/',views.CorreosNested_List.as_view()),
]
urlpatterns=format_suffix_patterns(urlpatterns)