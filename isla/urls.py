from django.contrib import admin
from django.urls import path
from . import views
urlpatterns = [
    path('', views.islas_view, name='islas_view'),
    path('<int:id>', views.isla_view, name='isla_view'),
]