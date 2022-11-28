import json
from django.shortcuts import render
from django.core import serializers
from http.client import HTTPResponse
from .logic import cliente_logic as lg

def clientes_view(request):
    if request.method == 'GET':
        clientes = lg.get_clientes()
        clientes_dto = serializers.serialize('json', clientes)
        return HTTPResponse(clientes_dto, content_type='application/json')
    elif request.method == 'POST':
        cliente_dto = lg.create_cliente(json.loads(request.body))
        cliente = serializers.serialize('json', [cliente_dto])
        return HTTPResponse(cliente, content_type='application/json')

def cliente_view(request, id):
    if request.method == 'GET':
        cliente = lg.get_cliente_by_id(id)
        cliente_dto = serializers.serialize('json', [cliente])
        return HTTPResponse(cliente_dto, content_type='application/json')