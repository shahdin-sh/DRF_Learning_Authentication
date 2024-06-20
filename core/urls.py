from django.urls import path, include
from .views import TokenDestroy, TokenCreate


urlpatterns = [
    path('token-create/', TokenCreate.as_view(), name='token-create'),
    path('token-destroy/', TokenDestroy.as_view(), name='token-destroy')
]