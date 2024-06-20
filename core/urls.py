from django.urls import path, include
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    path('obtain-auth-token/', obtain_auth_token, name='obtain_auth_token'),
]