import json
from django.shortcuts import render
from django.core import serializers
from http.client import HTTPResponse
from .logic import isla_logic as lg
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def islas_view(request):
    if request.method == 'GET':
        islas = lg.get_islas()
        islas_dto = serializers.serialize('json', islas)
        return HTTPResponse(islas_dto, 'application/json')
    elif request.method == 'POST':
        isla_dto = lg.create_isla(json.loads(request.body))
        isla = serializers.serialize('json', [isla_dto])
        return HTTPResponse(isla, 'application/json')

@csrf_exempt
def isla_view(request, id):
    if request.method == 'GET':
        isla = lg.get_isla_by_id(id)
        isla_dto = serializers.serialize('json', [isla])
        return HTTPResponse(isla_dto, 'application/json')