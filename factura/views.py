from django.shortcuts import render
import json
from django.core import serializers
from django.http import HttpResponse
from .logic import factura_logic as lg
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def facturas_view(request):
    if request.method == 'GET':
        facturas = lg.get_facturas()
        facturas_dto = serializers.serialize('json', facturas)
        return HttpResponse(facturas_dto, 'application/json')
    elif request.method == 'POST':
        factura_dto = lg.create_factura(json.loads(request.body))
        for detail in json.loads(request.body)['factura_detalle']:
            lg.create_factura_detail(detail, factura_dto)
        factura = serializers.serialize('json', [factura_dto])
        return HttpResponse(factura, 'application/json')

@csrf_exempt
def factura_view(request, id):
    if request.method == 'GET':
        factura = lg.get_factura_by_id(id)
        factura_dto = serializers.serialize('json', [factura])
        return HttpResponse(factura_dto, 'application/json')

@csrf_exempt
def factura_detail_view(request, id):
    if request.method == 'GET':
        factura_detail = lg.get_factura_detail_by_id_factura(id)
        factura_detail_dto = serializers.serialize('json', factura_detail)
        return HttpResponse(factura_detail_dto, 'application/json')
