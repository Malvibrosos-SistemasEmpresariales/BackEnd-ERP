from django.contrib import admin
from django.urls import path
from . import views
urlpatterns = [
    path('', views.inventarios_view, name='inventarios_view'),
    path('<int:id>', views.inventario_view, name='inventario_view'),
]