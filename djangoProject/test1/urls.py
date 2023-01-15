from django.urls import path
from . import views

# from django.contrib import admin
# from django.urls import path, include  配置前后端分离时需要


urlpatterns=[
    path('post/',views.result,name='webgis')

]