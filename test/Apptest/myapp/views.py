from django.shortcuts import render
from django.db.models import Q
from .serializers import StoreListSerializer
from .serializers import MenuListSerializer
#from . serializers import OrderInfoSerializer,OrderListSerializer,OrderMenuSerializer
#from .models import OrderList,OrderInfo,OrderMenu
from .models import StoreList, MenuList
from rest_framework import filters
from rest_framework import viewsets
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.parsers import JSONParser
from rest_framework.response import Response
from rest_framework.views import APIView
import request

from rest_framework import generics
 # Create your views here.


class StoreListViewSet(viewsets.ModelViewSet):
    queryset = StoreList.objects.all()
    serializer_class = StoreListSerializer
    filter_backends = (filters.SearchFilter,  filters.OrderingFilter,  DjangoFilterBackend)
    #filter_backends = (filters.SearchFilter, filters.OrderingFilter)
    filter_fields = ('latitude', 'longitude')

class MenuListViewSet(viewsets.ModelViewSet):
    queryset = MenuList.objects.all()
    serializer_class = MenuListSerializer
    filter_backends = (filters.SearchFilter, filters.OrderingFilter, DjangoFilterBackend)
    #filter_backends = (filters.SearchFilter, filters.OrderingFilter)
    filter_fields = ['store_id']

'''
class OrderListViewSet(APIView):
    parser_classes = (JSONParser,)

    def post(self, request, format=None):
        return Response({'received data': request.data})
'''



'''
class OrderListViewSet(viewsets.ModelViewSet):
    queryset = OrderList.objects.all()
    serializer_class = OrderListSerializer
    filter_backends = (filters.SearchFilter, filters.OrderingFilter, DjangoFilterBackend)
    filters_fields = ('store_id', 'order_id')

'''

'''
class StoreListViewSet(generics.ListAPIView):
    serializer_class = StoreListSerializer


    def get_queryset(self):
        queryset = StoreList.objects.all()
        store_id = self.request.query_params.get('store_id',None)
        if store_id is not None:
            queryset = queryset.filter(STORE_ID=store_id)
        return queryset

'''
