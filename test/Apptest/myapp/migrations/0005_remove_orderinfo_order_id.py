# Generated by Django 2.1.3 on 2018-12-22 14:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0004_orderlist_order_info'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='orderinfo',
            name='order_id',
        ),
    ]