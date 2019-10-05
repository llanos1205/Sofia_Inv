from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token  # <-- Here
from Sofia_Server.core import views
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
     path('hello/', views.HelloView.as_view(), name='hello'),
     path('api-token-auth/', obtain_auth_token, name='api_token_auth'),
]