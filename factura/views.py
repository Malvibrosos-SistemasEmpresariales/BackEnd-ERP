from django.shortcuts import render
import json
from django.core import serializers
from http.client import HTTPResponse
from .logic import factura_logic as lg

def facturas_view(request):
    if request.method == 'GET':
        facturas = lg.get_facturas()
        facturas_dto = serializers.serialize('json', facturas)
        return HTTPResponse(facturas_dto, content_type='application/json')
    elif request.method == 'POST':
        factura_dto = lg.create_factura(json.loads(request.body))
        factura = serializers.serialize('json', [factura_dto])
        return HTTPResponse(factura, content_type='application/json')

def factura_view(request, id):
    if request.method == 'GET':
        factura = lg.get_factura_by_id(id)
        factura_dto = serializers.serialize('json', [factura])
        return HTTPResponse(factura_dto, content_type='application/json')
