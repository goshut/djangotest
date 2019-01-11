from django.shortcuts import render, reverse, redirect
from django.http import HttpResponse, JsonResponse
import json

# Create your views here.
def index(request):
    return JsonResponse([{
        'age': 78,
        'name': 'keke',
    }, {
        'lll':456,
        'name':'oijpo'
    }], safe=False)


def hand(request, a, b):
    print(a)
    print(b)
    return HttpResponse('hand', content_type='text/html', status=200)


def post(request):
    # json1 = request.body
    # # json1 = json1.decode()
    # data = json.loads(json1)
    # print(data)
    return redirect(reverse('users:index'))
