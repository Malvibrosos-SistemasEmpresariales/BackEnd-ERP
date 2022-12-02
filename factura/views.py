from django.shortcuts import render
import json
from django.core import serializers
from django.http import HttpResponse, HttpResponseRedirect
from django.http.response import JsonResponse
from django.urls import reverse
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
        factura_detail = lg.get_factura_detail_by_id_factura(id)
        list_detail = []
        for detail in factura_detail:
            list_detail.append(
                FacturaDetailSerializer(detail).data)
        facturas_serializer = FacturaSerializer(factura, many=False).data
        facturas_serializer['factura_detalle'] = list_detail
        return JsonResponse(facturas_serializer, safe=False)
    elif request.method == 'DELETE':
        factura = lg.delete_factura(id)
        return JsonResponse({'message': '{} Factura were deleted successfully!'.format(id)})

@csrf_exempt
def factura_detail_view(request, id):
    if request.method == 'GET':
        factura_detail = lg.get_factura_detail_by_id_factura(id)
        factura_detail_serializer = FacturaDetailSerializer(factura_detail, many=True)
        return JsonResponse(factura_detail_serializer.data, safe=False)

def factura_view_by_date(request, date):
    if request.method == 'GET':
        facturas = lg.get_factura_by_date(date)
        facturas_serializer = FacturaSerializer(facturas, many=True)
        return JsonResponse(facturas_serializer.data, safe=False)
