# Generated by Django 2.1.3 on 2018-12-22 14:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0002_auto_20181222_2330'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='orderlist',
            name='order_info',
        ),
    ]
