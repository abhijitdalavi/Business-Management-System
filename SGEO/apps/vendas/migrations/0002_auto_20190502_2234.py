# Generated by Django 2.0.5 on 2019-05-03 01:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vendas', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='condicaopagamento',
            name='dia_pagamento',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='condicaopagamento',
            name='flag_dia_pagamento',
            field=models.BooleanField(default=False),
        ),
    ]
