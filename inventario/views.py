import json
from django.shortcuts import render
from django.core import serializers
from http.client import HTTPResponse
from .logic import inventario_logic as lg

def inventarios_view(request):
    if request.method == 'GET':
        inventarios = lg.get_inventarios()
        inventarios_dto = serializers.serialize('json', inventarios)
        return HTTPResponse(inventarios_dto, content_type='application/json')
    elif request.method == 'POST':
        inventario_dto = lg.create_inventario(json.loads(request.body))
        inventario = serializers.serialize('json', [inventario_dto])
        return HTTPResponse(inventario, content_type='application/json')

def inventario_view(request, id):
    if request.method == 'GET':
        inventario = lg.get_inventario_by_id(id)
        inventario_dto = serializers.serialize('json', [inventario])
        return HTTPResponse(inventario_dto, content_type='application/json')