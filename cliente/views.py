import json
from django.shortcuts import render
from django.core import serializers
from django.http import HttpResponse
from .logic import cliente_logic as lg
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def clientes_view(request):
    if request.method == 'GET':
        clientes = lg.get_clientes()
        clientes_dto = serializers.serialize('json', clientes)
        return HttpResponse(clientes_dto,'application/json')
    elif request.method == 'POST':
        cliente_dto = lg.create_cliente(json.loads(request.body))
        cliente = serializers.serialize('json', [cliente_dto])
        return HttpResponse(cliente, 'application/json')

@csrf_exempt
def cliente_view(request, id):
    if request.method == 'GET':
        cliente = lg.get_cliente_by_id(id)
        cliente_dto = serializers.serialize('json', [cliente])
        return HttpResponse(cliente_dto, content_type='application/json')