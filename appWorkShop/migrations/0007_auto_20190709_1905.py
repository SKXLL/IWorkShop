# Generated by Django 2.1.2 on 2019-07-09 23:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appWorkShop', '0006_auto_20190709_1814'),
    ]

    operations = [
        migrations.AddField(
            model_name='profesor',
            name='apellidoProfe',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='profesor',
            name='nombreProfe',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
