from django.urls import path
from Sofia_Server.core import views
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
     path('hello/', views.HelloView.as_view(), name='hello'),
]