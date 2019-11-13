from django.urls import path
from Sofia_Server.Sofia_App.Modulos.Transacciones import views
from rest_framework.urlpatterns import format_suffix_patterns
urlpatterns = [
  path('Auditorias/',views.Auditoria_List.as_view()),
    path('Auditorias/<int:pk>/',views.Auditoria_Detail.as_view()),
    path('Auditorias/Nested/',views.AuditoriaNested_List.as_view()),
    path('Asociaciones/',views.Asociacion_List.as_view()),
    path('Asociaciones/<int:pk>/',views.Asociacion_Detail.as_view()),
    path('Asociaciones/Nested/',views.AsociacionNested_List.as_view()),
]
urlpatterns=format_suffix_patterns(urlpatterns)