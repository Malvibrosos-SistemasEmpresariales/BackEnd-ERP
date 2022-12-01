import json
from django.shortcuts import render
from django.core import serializers
from django.http import HttpResponse
from django.http.response import JsonResponse
from serializers import IslaSerializer
from .logic import isla_logic as lg
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def islas_view(request):
    if request.method == 'GET':
        islas = lg.get_islas()
        islas_dto = IslaSerializer(islas, many=True)
        return JsonResponse(islas_dto.data, safe=False)
    elif request.method == 'POST':
        isla_dto = lg.create_isla(json.loads(request.body))
        isla = serializers.serialize('json', [isla_dto])
        return HttpResponse(isla, 'application/json')

@csrf_exempt
def isla_view(request, id):
    if request.method == 'GET':
        isla = lg.get_isla_by_id(id)
        isla_dto = IslaSerializer(isla, many=False)
        return JsonResponse(isla_dto.data, safe=False)