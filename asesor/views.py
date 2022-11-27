from http.client import HTTPResponse
from django.shortcuts import render
from django.core import serializers
from logic import lg

def asesores_view(request):
    if request.method == 'GET':
        asesores = lg.get_asesores()
        asesores_dto = serializers.serialize('json', asesores)
        return HTTPResponse(asesores_dto, content_type='application/json')