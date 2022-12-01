import json
from django.core import serializers
from django.http import HttpResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.http.response import JsonResponse

from serializers import ProductoSerializer
from .logic import producto_logic as lg

@csrf_exempt
def productos_view(request):
    if request.method == 'GET':
        productos = lg.get_productos()
        productos_dto = ProductoSerializer(productos, many=True)
        return JsonResponse(productos_dto.data, safe=False)
    elif request.method == 'POST':
        producto_dto = lg.create_producto(json.loads(request.body))
        producto = serializers.serialize('json', [producto_dto])
        return HttpResponse(producto, content_type='application/json')

@csrf_exempt
def producto_view(request, id):
    if request.method == 'GET':
        producto = lg.get_producto_by_id(id)
        producto_dto = ProductoSerializer(producto, many=False)
        return JsonResponse(producto_dto.data, safe=False)