# Generated by Django 4.0 on 2022-01-10 19:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('koszyk', '0021_adres_order_adres'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='adres',
        ),
    ]
