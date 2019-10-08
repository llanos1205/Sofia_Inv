from django.urls import path
from Sofia_Server.Sofia_App.Modulos.InfoUser import views
from rest_framework.urlpatterns import format_suffix_patterns
urlpatterns = [
     path('Empresas/',views.EmpresaList.as_view()),
    path('Empresas/<int:pk>/',views.Empresa_Detail.as_view()),
   
    path('Departamentos/',views.Departamento_List.as_view()),
    path('Departamentos/<int:pk>/',views.Departamento_Detail.as_view()),
   
    path('Areas/',views.Area_List.as_view()),
    path('Areas/<int:pk>/',views.Area_Detail.as_view()),
   
    path('Regionales/',views.Regional_List.as_view()),
    path('Regionales/<int:pk>/',views.Regional_Detail.as_view()),
   
    path('Ubicaciones/',views.Ubicacion_List.as_view()),
    path('Ubicaciones/<int:pk>/',views.Ubicacion_Detail.as_view()),
   
    path('Gerencias/',views.Gerencia_List.as_view()),
    path('Gerencias/<int:pk>/',views.Gerencia_Detail.as_view()),

    path('Cargos/',views.Cargo_List.as_view()),
    path('Cargos/<int:pk>/',views.Cargo_Detail.as_view()),
    path('Permisos/',views.Permiso_List.as_view()),
    path('Permisos/<int:pk>/',views.Permiso_Detail.as_view()),

]
urlpatterns=format_suffix_patterns(urlpatterns)
