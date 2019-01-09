from django.shortcuts import render, reverse
from django.http import HttpResponse
import json

# Create your views here.
def index(request):
    return HttpResponse('hehehhehe')


def hand(request, a, b):
    print(a)
    print(b)
    return HttpResponse('\t'+a+'\t'+b)


def post(request):
    json1 = request.body
    # json1 = json1.decode()
    data = json.loads(json1)
    print(data)
    return HttpResponse('OK')
