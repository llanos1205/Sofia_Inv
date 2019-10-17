from rest_framework.urlpatterns import format_suffix_patterns
from django.urls import path
from Sofia_Server.Sofia_App.Modulos.Equipos import views
urlpatterns = [
    path('Equipos/',views.Equipo_List.as_view()),
    path('Equipos/<int:pk>/',views.Equipo_Detail.as_view()),
    path('Equipos/Nested/',views.EquipoNested_List.as_view()),
    path('Ordenadores/',views.Ordenador_List.as_view()),
    path('Ordenadores/<int:pk>/',views.Ordenador_Detail.as_view()),
    path('Ordenadores/Nested/',views.OrdenadorNested_List.as_view()),
    path('Otrodispositivos/',views.OtroDispositivo_List.as_view()),
    path('Otrodispositivos/<int:pk>',views.OtroDispositivo_Detail.as_view()),
    path('Otrodispositivos/Nested/',views.OtroDispositivosNested_List.as_view()),
    path('Impresoras/',views.Impresora_List.as_view()),
    path('Impresoras/<int:pk>',views.Impresora_Detail.as_view()),
    path('Impresoras/Nested/',views.ImpresoraNested_List.as_view()),
    path('Licencias/',views.Licencia_List.as_view()),
    path('Licencias/<int:pk>',views.Licencia_Detail.as_view()),
    path('Atributos/',views.Atributo_List.as_view()),
    path('Atributos/<int:pk>',views.Atributo_Detail.as_view()),
    path('Equipo_Atributos/',views.Equipo_Atributo_List.as_view()),
    path('Oss/',views.Os_List.as_view()),
    path('Oss/<int:pk>',views.Os_Detail.as_view()),
    path('Equipos_Atributos/',views.Equipo_Atributo_List.as_view()),
    path('Equipos_Atributos/<int:pk>/<int:pk2>/',views.Equipo_Atributo_Detail.as_view()),
    path('Ordenador_Licencias/',views.OrdenadorHasLicencia_List.as_view()),
    path('Ordenador_Licencias/Nested/',views.OrdenadorHasLicenciaNested_List.as_view()),
    path('Ordenador_Licencias/<int:pk2>/<int:pk3>/',views.OrdenadorHasLicencia_Detail.as_view()),
    path('Tablets/',views.Tablet_List.as_view()),
    path('Tablets/<int:pk>',views.Tablet_Detail.as_view()),
    
]
urlpatterns=format_suffix_patterns(urlpatterns)
