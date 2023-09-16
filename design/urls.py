# urls.py
from django.urls import path
from .views import *



urlpatterns = [
    path('', index, name='index'),
    path('ww/', WW, name='WW'),
    path('dn/', dn, name='dn'),
    path('getValue/',getValue, name='getValue'),
    path('setww/',setww, name='setww'),
]