# Generated by Django 4.2.9 on 2024-03-24 15:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0009_offerbanner'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='OrderItems',
            field=models.ManyToManyField(through='core.OrderItem', to='core.product'),
        ),
    ]