# Generated by Django 4.0 on 2022-01-08 22:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('koszyk', '0012_rename_product_cart_products'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cart',
            name='products',
        ),
        migrations.AddField(
            model_name='cart',
            name='products',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='koszyk.cartitem'),
        ),
    ]
