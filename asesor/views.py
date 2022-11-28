import json
from django.http import HttpResponse
from django.shortcuts import render
from django.core import serializers
from .logic import logic_asesor as lg

def asesores_view(request):
    if request.method == 'GET':
        asesores = lg.get_asesores()
        asesores_dto = serializers.serialize('json', asesores)
        return HttpResponse(asesores_dto, 'application/json')
    elif request.method == 'POST':
        asesor_dto = lg.create_asesor(json.loads(request.body))
        asesor = serializers.serialize('json', [asesor_dto])
        return HttpResponse(asesor,'application/json')

def asesor_view(request, id):
    if request.method == 'GET':
        asesor = lg.get_asesor_by_id(id)
        asesor_dto = serializers.serialize('json', [asesor])
        return HttpResponse(asesor_dto,'application/json')