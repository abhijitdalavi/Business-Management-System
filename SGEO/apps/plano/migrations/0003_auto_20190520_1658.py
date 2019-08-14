# Generated by Django 2.0.5 on 2019-05-20 19:58

from decimal import Decimal
import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('plano', '0002_auto_20190519_2108'),
    ]

    operations = [
        migrations.CreateModel(
            name='Pagamento',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data_criacao', models.DateField()),
                ('data_pagamento', models.DateField(blank=True, null=True)),
                ('data_vencimento', models.DateField(blank=True, null=True)),
                ('status', models.CharField(choices=[('1', 'Aguardando pagamento'), ('2', 'Em análise'), ('3', 'Paga'), ('4', 'Disponível'), ('5', 'Em disputa'), ('6', 'Devolvida'), ('7', 'Cancelada')], default=1, max_length=1)),
                ('codigo', models.CharField(blank=True, max_length=100, null=True)),
                ('valor', models.DecimalField(decimal_places=2, max_digits=12, validators=[django.core.validators.MinValueValidator(Decimal('0.00'))])),
            ],
        ),
        migrations.RemoveField(
            model_name='pagamentos',
            name='plano',
        ),
        migrations.DeleteModel(
            name='Pagamentos',
        ),
    ]
