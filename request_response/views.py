from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.
def redis_store(request):
    request.session['name'] = 'ppp'
    print(request.session['name'])
    return HttpResponse('ll')
