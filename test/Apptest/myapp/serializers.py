from .models import MenuList
from .models import StoreList
#from .models import OrderMenu,OrderInfo,OrderList
from rest_framework import serializers


class StoreListSerializer(serializers.HyperlinkedModelSerializer):
     image = serializers.ImageField(use_url=True)
     class Meta:
         model = StoreList
         fields = ('image', 'store_id','name', 'phone', 'latitude', 'longitude')


class MenuListSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = MenuList
        fields = ('store_id', 'menu_number', 'menu_name', 'menu_price')

'''
class OrderMenuSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = OrderMenu
        fields = ('order_menu', 'order_amount')

class OrderInfoSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = OrderInfo
        fields = ('order_name', 'order_phone_num')

class OrderListSerializer(serializers.HyperlinkedModelSerializer):
    order_list = OrderMenuSerializer(many=True, ead_only=True)
    order_info = OrderInfoSerializer(many=True, read_only=True)

    class Meta:
        model = OrderList
        fields = ('orderInfo', 'orderList', 'order_id', 'store_id')
        read_only_fields = ('orderList', 'orderInfo')
'''