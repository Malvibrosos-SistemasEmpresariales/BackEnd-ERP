from django.contrib import admin
from django.urls import path
from . import views
urlpatterns = [
    path('', views.inventarios_view, name='inventarios_view'),
    path('<int:id>', views.inventario_view, name='inventario_view'),
    path('movimientos/<int:id>', views.movimientos_productos_view, name='movimientos_productos_view'),
    path('movimientos/', views.movimientos_view, name='movimientos_view'),
]