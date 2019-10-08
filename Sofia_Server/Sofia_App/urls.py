from django.urls import path,include
from Sofia_Server.Sofia_App.Modulos import InfoUser,Transacciones,Equipos,Usuarios
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    # path('Equipos/', views.Equipo_list),
    # path('Equipos/<int:pk>/', views.Equipo_detail),
  
   
    
    
]
urlpatterns=format_suffix_patterns(urlpatterns)
