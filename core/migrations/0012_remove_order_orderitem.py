# Generated by Django 4.2.9 on 2024-03-24 15:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0011_rename_orderitems_order_orderitem'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='OrderItem',
        ),
    ]