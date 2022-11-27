from django.contrib import admin
from django.urls import path
from . import views
urlpatterns = [
    path('', views.asesores_view, name='asesores_view'),
    path('<int:id>', views.asesor_view, name='asesor_view'),
]