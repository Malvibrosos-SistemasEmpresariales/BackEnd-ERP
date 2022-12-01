from django.contrib import admin
from django.urls import path
from . import views
urlpatterns = [
    path('', views.facturas_view, name='facturas_view'),
    path('<int:id>', views.factura_view, name='factura_view'),
    path('detail/<int:id>', views.factura_detail_view, name='factura_detail_view'),
    path('date/<str:date>', views.factura_view_by_date, name='factura_view_by_date'),
]