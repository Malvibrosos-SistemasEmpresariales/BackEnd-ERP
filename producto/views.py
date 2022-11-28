import json
from django.core import serializers
from http.client import HTTPResponse
from django.shortcuts import render

from .logic import producto_logic as lg

def productos_view(request):
    if request.method == 'GET':
        productos = lg.get_productos()
        productos_dto = serializers.serialize('json', productos)
        return HTTPResponse(productos_dto, content_type='application/json')
    elif request.method == 'POST':
        producto_dto = lg.create_producto(json.loads(request.body))
        producto = serializers.serialize('json', [producto_dto])
        return HTTPResponse(producto, content_type='application/json')

def producto_view(request, id):
    if request.method == 'GET':
        producto = lg.get_producto_by_id(id)
        producto_dto = serializers.serialize('json', [producto])
        return HTTPResponse(producto_dto, content_type='application/json')