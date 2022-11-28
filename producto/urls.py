from django.contrib import admin
from django.urls import path
from . import views
urlpatterns = [
    path('', views.productos_view, name='productos_view'), 
    path('<int:id>', views.producto_view, name='producto_view'),
]