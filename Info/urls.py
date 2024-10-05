from django.urls import path
from .views import Device
urlpatterns = [
    path('device/',Device,name='Device Info')   
]
