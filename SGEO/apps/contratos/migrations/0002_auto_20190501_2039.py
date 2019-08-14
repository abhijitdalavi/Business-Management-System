# Generated by Django 2.0.5 on 2019-05-01 23:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('vendas', '0001_initial'),
        ('cadastro', '0001_initial'),
        ('contratos', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='contrato',
            name='condicao_pagamento',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='contrato_pagamento', to='vendas.CondicaoPagamento'),
        ),
        migrations.AddField(
            model_name='contrato',
            name='empresa',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='contrato_empresa', to='cadastro.Empresa'),
        ),
        migrations.AddField(
            model_name='contrato',
            name='tipo_contrato',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='contrato_tipo', to='contratos.TipoContrato'),
        ),
        migrations.AddField(
            model_name='contrato',
            name='vendedor',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='contrato_vendedor', to='cadastro.Vendedor'),
        ),
    ]