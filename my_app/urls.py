from django.urls import path
from .views import home

urlpatterns = [
    path('', home, name='home'),
    # You can define more URL patterns for other views
]
