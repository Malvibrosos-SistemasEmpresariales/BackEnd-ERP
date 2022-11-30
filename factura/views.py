from django.shortcuts import render
import json
from django.core import serializers
from django.http import HttpResponse
from django.http.response import JsonResponse
from .logic import factura_logic as lg
from django.views.decorators.csrf import csrf_exempt
from serializers import FacturaSerializer, FacturaDetailSerializer

@csrf_exempt
def facturas_view(request):
    if request.method == 'GET':
        facturas = lg.get_facturas()
        facturas_serializer = FacturaSerializer(facturas, many=True)
        return JsonResponse(facturas_serializer.data, safe=False)
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
        facturas_serializer = FacturaSerializer(factura, many=False)
        return JsonResponse(facturas_serializer.data, safe=False)

@csrf_exempt
def factura_detail_view(request, id):
    if request.method == 'GET':
        factura_detail = lg.get_factura_detail_by_id_factura(id)
        factura_detail_serializer = FacturaDetailSerializer(factura_detail, many=True)
        return JsonResponse(factura_detail_serializer.data, safe=False)
