import json
from django.shortcuts import render
from django.core import serializers
from http.client import HTTPResponse
from .logic import logic_isla as lg

def islas_view(request):
    if request.method == 'GET':
        islas = lg.get_islas()
        islas_dto = serializers.serialize('json', islas)
        return HTTPResponse(islas_dto, content_type='application/json')
    elif request.method == 'POST':
        isla_dto = lg.create_isla(json.loads(request.body))
        isla = serializers.serialize('json', [isla_dto])
        return HTTPResponse(isla, content_type='application/json')

def isla_view(request, id):
    if request.method == 'GET':
        isla = lg.get_isla_by_id(id)
        isla_dto = serializers.serialize('json', [isla])
        return HTTPResponse(isla_dto, content_type='application/json')