# Generated by Django 4.2.9 on 2024-03-23 04:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0008_order_staff'),
    ]

    operations = [
        migrations.CreateModel(
            name='OfferBanner',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('description', models.TextField()),
                ('image', models.ImageField(upload_to='offer_banner/')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]