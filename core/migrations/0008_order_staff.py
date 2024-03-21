# Generated by Django 4.2.9 on 2024-03-21 04:21

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('core', '0007_remove_order_total_price_order_created_at_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='staff',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='staff', to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
    ]