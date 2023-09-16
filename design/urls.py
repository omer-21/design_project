# urls.py
from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name='index'),
    path('ww/', WW, name='WW'),
    path('getValue/',getValue, name='getValue'),
]