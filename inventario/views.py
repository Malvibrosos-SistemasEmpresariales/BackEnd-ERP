import json
from django.shortcuts import render
from django.core import serializers
from django.http import HttpResponse
from .logic import inventario_logic as lg
from django.http.response import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from serializers import InventarioSerializer, InventarioDetailSerializer

@csrf_exempt
def inventarios_view(request):
    if request.method == 'GET':
        inventarios = lg.get_inventarios()
        inventarios_dto = InventarioSerializer(inventarios, many=True)
        return JsonResponse(inventarios_dto.data, safe=False)
    elif request.method == 'POST':
        inventario_dto = lg.create_inventario(json.loads(request.body))
        inventario = serializers.serialize('json', [inventario_dto])
        return HttpResponse(inventario, 'application/json')

@csrf_exempt
def inventario_view(request, id):
    if request.method == 'GET':
        inventario = lg.get_inventario_by_id(id)
        inventario_detail = lg.get_movimientos_by_id_producto(id)
        list_movimientos = []
        for movimiento in inventario_detail:
            list_movimientos.append(InventarioDetailSerializer(movimiento).data)
        inventario_dto = InventarioSerializer(inventario, many=False).data
        inventario_dto['movimientos'] = list_movimientos
        return JsonResponse(inventario_dto, safe=False)

@csrf_exempt
def movimientos_productos_view(request, id):
    if request.method == 'GET':
        movimientos = lg.get_movimientos_by_id_producto(id)
        movimientos_dto = InventarioDetailSerializer(movimientos, many=True)
        return JsonResponse(movimientos_dto.data, safe=False)

@csrf_exempt
def movimientos_view(request):
    if request.method == 'POST':
        movimiento_dto = lg.create_movimiento(json.loads(request.body))
        movimiento = serializers.serialize('json', [movimiento_dto])
        return HttpResponse(movimiento, 'application/json')