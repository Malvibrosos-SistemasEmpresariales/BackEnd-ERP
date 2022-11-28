from django.contrib import admin
from django.urls import path
from . import views
urlpatterns = [
    path('', views.facturas_view, name='facturas_view'),
    path('<int:id>', views.factura_view, name='factura_view'),
]