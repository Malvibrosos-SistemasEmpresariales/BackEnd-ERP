import json
from django.shortcuts import render
from django.core import serializers
from django.http import HttpResponse
from .logic import inventario_logic as lg
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def inventarios_view(request):
    if request.method == 'GET':
        inventarios = lg.get_inventarios()
        inventarios_dto = serializers.serialize('json', inventarios)
        return HttpResponse(inventarios_dto, 'application/json')
    elif request.method == 'POST':
        inventario_dto = lg.create_inventario(json.loads(request.body))
        inventario = serializers.serialize('json', [inventario_dto])
        return HttpResponse(inventario, 'application/json')

@csrf_exempt
def inventario_view(request, id):
    if request.method == 'GET':
        inventario = lg.get_inventario_by_id(id)
        inventario_dto = serializers.serialize('json', [inventario])
        return HttpResponse(inventario_dto,'application/json')

@csrf_exempt
def movimientos_productos_view(request, id):
    if request.method == 'GET':
        movimientos = lg.get_movimientos_by_id_producto(id)
        movimientos_dto = serializers.serialize('json', movimientos)
        return HttpResponse(movimientos_dto, 'application/json')