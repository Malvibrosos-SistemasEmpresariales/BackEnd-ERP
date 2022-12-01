import json
from django.http import HttpResponse
from django.shortcuts import render
from django.core import serializers

from serializers import AsesorSerializer
from .logic import logic_asesor as lg
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def asesores_view(request):
    if request.method == 'GET':
        asesores = lg.get_asesores()
        asesores_dto = AsesorSerializer(asesores, many=True)
        return HttpResponse(asesores_dto.data, 'application/json')
    elif request.method == 'POST':
        asesor_dto = lg.create_asesor(json.loads(request.body))
        asesor = serializers.serialize('json', [asesor_dto])
        return HttpResponse(asesor,'application/json')

@csrf_exempt
def asesor_view(request, id):
    if request.method == 'GET':
        asesor = lg.get_asesor_by_id(id)
        asesor_dto = AsesorSerializer(asesor, many=False)
        return HttpResponse(asesor_dto.data,'application/json')