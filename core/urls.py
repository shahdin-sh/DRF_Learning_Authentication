from django.urls import path, include
from .views import TokenDestroyView, TokenCreateView, UserRegistrationView, UserView


urlpatterns = [
    path('token-create/', TokenCreateView.as_view(), name='token-create'),
    path('token-destroy/', TokenDestroyView.as_view(), name='token-destroy'),
    path('user-registration/', UserRegistrationView.as_view(), name='user-registration'),
    path('user/', UserView.as_view(), name='user')
]