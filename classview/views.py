from django.shortcuts import render
from django.views import View
from django.http import HttpResponse, JsonResponse
from django.utils.decorators import method_decorator
from rest_framework.generics import GenericAPIView, RetrieveUpdateDestroyAPIView, ListAPIView
from rest_framework.mixins import ListModelMixin
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet

from classview.models import Book
from classview.serializers import Bookserializers, BookInfoSerializer


class Bookview(ListModelMixin, GenericAPIView):
    queryset = Book.objects.all()
    serializer_class = BookInfoSerializer
    def get(self, request, pk):
        return self.list(request)

    # def get(self, request, pk):
    #     book = self.get_object()  # get_object()方法根据pk参数查找queryset中的数据对象
    #     serializer = self.get_serializer(book)
    #     return Response(serializer.data)