from django.urls import path, include
from .views import welcome_view

urlpatterns = [
    path('', welcome_view, name='welcome-view'),
]