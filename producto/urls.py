from django.contrib import admin
from django.urls import path
from . import views
urlpatterns = [
    path('', views.productos_view, name='productos_view'),
    # set id path with a string
    path('<str:id>', views.producto_view, name='producto_view'),
]
