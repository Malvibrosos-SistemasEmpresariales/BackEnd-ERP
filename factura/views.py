from django.shortcuts import render
import json
from django.core import serializers
from django.http import HttpResponse
from .logic import factura_logic as lg

def facturas_view(request):
    if request.method == 'GET':
        facturas = lg.get_facturas()
        facturas_dto = serializers.serialize('json', facturas)
        return HttpResponse(facturas_dto, 'application/json')
    elif request.method == 'POST':
        factura_dto = lg.create_factura(json.loads(request.body))
        factura = serializers.serialize('json', [factura_dto])
        return HttpResponse(factura, 'application/json')

def factura_view(request, id):
    if request.method == 'GET':
        factura = lg.get_factura_by_id(id)
        factura_dto = serializers.serialize('json', [factura])
        return HttpResponse(factura_dto, 'application/json')
