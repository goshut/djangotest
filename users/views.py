from django.shortcuts import render, reverse
from django.http import HttpResponse

# Create your views here.
def index(request):
    return HttpResponse('hehehhehe')


def hand(request, a, b):
    print(a)
    print(b)
    return HttpResponse('\t'+a+'\t'+b)


def post(request):
    json1 = request.body
