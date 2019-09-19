from django.urls import path
from Sofia_Server.Sofia_App import views
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    # path('Equipos/', views.Equipo_list),
    # path('Equipos/<int:pk>/', views.Equipo_detail),
    path('Empresas/',views.EmpresaList.as_view()),
    path('Empresas/<int:pk>/',views.Empresa_Detail.as_view()),
]
urlpatterns=format_suffix_patterns(urlpatterns)