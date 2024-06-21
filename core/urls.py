from django.urls import path, include
from .views import TokenDestroyView, TokenCreateView, UserRegistrationView


urlpatterns = [
    path('user-registration/', UserRegistrationView.as_view(), name='user-registration'),
    path('token-create/', TokenCreateView.as_view(), name='token-create'),
    path('token-destroy/', TokenDestroyView.as_view(), name='token-destroy'),
]