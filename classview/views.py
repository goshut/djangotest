from django.shortcuts import render
from django.views import View
from django.http import HttpResponse
from django.utils.decorators import method_decorator

# Create your views here.


def decorator1(fun):
    def wrapper(request, *args, **kwargs):
        print('装饰了')
        return fun(request, *args, **kwargs)
    return wrapper


@method_decorator(decorator1, name='dispatch')
class View1(View):

    def get(self, request):
        return HttpResponse('GET')

    def post(self, request):
        return HttpResponse('post')

