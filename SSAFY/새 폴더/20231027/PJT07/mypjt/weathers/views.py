from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
import requests


# Create your views here.
@api_view(['GET'])
def index(request):
    api_key = '7654c6d1a20cf7c8fafb30993d74d881'
    city = 'Seoul,KR'
    url = f'https://api.openweathermap.org/data/2.5/forecast?q={city}&appid={api_key}'

    response = requests.get(url).json()

    return Response(response)