from django.db import models

# Create your models here.

'''
class OrderInfo(models.Model):
    order_name = models.CharField(max_length=20)
    order_phone = models.CharField(max_length=10)


class OrderMenu(models.Model):
    menu_name = models.CharField(max_length=20)
    menu_amount = models.CharField(max_length=20)
'''


class StoreList(models.Model):
    image = models.ImageField(default='media/default_image.jpeg')
    store_id = models.CharField(max_length=100)
    name = models.CharField(max_length=20)
    phone = models.CharField(max_length=20)
    latitude = models.CharField(max_length=20)
    longitude = models.CharField(max_length=20)


class MenuList(models.Model):
    store_id = models.CharField(max_length=100)
    menu_number = models.CharField(max_length=20)
    menu_name = models.CharField(max_length=20)
    menu_price = models.CharField(max_length=10)

'''
class OrderList(models.Model):
    order_info = models.ManyToManyField(OrderInfo)
    order_menu = models.ManyToManyField(OrderMenu)
    order_id = models.CharField(max_length=10)
    store_id = models.CharField(max_length=20)
'''






