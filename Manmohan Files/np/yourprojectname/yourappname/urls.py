from django.urls import path
from .views import map_view

urlpatterns = [
    path('showmap/', map_view, name='show_map'),
]
