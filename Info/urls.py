from django.urls import path
from .views import Device
urlpatterns = [
    path('device/<pdf_path>/<printer_name>/',Device,name='Device Info')   
]
