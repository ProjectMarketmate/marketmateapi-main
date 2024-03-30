# Generated by Django 4.2.9 on 2024-03-28 10:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0013_product_average_rating_rating'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='rating',
            name='created_at',
        ),
        migrations.AlterField(
            model_name='product',
            name='average_rating',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=3, null=True),
        ),
    ]