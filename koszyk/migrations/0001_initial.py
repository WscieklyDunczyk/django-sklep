# Generated by Django 4.0 on 2022-01-07 18:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('witryna', '0005_remove_cartitem_koszyk_remove_cartitem_produkt_and_more'),
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='Koszyk',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data_zamowienia', models.DateTimeField(auto_now_add=True)),
                ('id_zamowienia', models.CharField(max_length=200, null=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='auth.user')),
            ],
        ),
        migrations.CreateModel(
            name='KoszykPrzedmiot',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ilosc', models.IntegerField(default=1)),
                ('koszyk', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='koszyk.koszyk')),
                ('produkt', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='witryna.produkt')),
            ],
        ),
    ]
