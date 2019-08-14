# Generated by Django 2.0.5 on 2019-05-01 23:39

from decimal import Decimal
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BoletosAdicionais',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantidade', models.IntegerField(default=0)),
                ('valor', models.DecimalField(decimal_places=2, max_digits=12, validators=[django.core.validators.MinValueValidator(Decimal('0.00'))])),
            ],
        ),
        migrations.CreateModel(
            name='NotasAdicionais',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantidade', models.IntegerField(default=0)),
                ('valor', models.DecimalField(decimal_places=2, max_digits=12, validators=[django.core.validators.MinValueValidator(Decimal('0.00'))])),
            ],
        ),
        migrations.CreateModel(
            name='Pagamentos',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ultimo_pagamento', models.DateField()),
                ('valor_ultimo_pagamento', models.DecimalField(decimal_places=2, max_digits=12, validators=[django.core.validators.MinValueValidator(Decimal('0.00'))])),
                ('proximo_pagamento', models.DateField()),
                ('valor_proximo_pagamento', models.DecimalField(decimal_places=2, max_digits=12, validators=[django.core.validators.MinValueValidator(Decimal('0.00'))])),
            ],
        ),
        migrations.CreateModel(
            name='Plano',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data_inicio', models.DateField()),
                ('tipo_pagamento', models.CharField(choices=[('0', 'Mensal'), ('1', 'Anual')], default=0, max_length=1)),
                ('valor', models.DecimalField(decimal_places=2, max_digits=12, validators=[django.core.validators.MinValueValidator(Decimal('0.00'))])),
                ('status_ativo', models.BooleanField(default=True)),
                ('boletos_adicionais', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='boletos_adicionais', to='plano.BoletosAdicionais')),
                ('notas_adicionais', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='notas_adicionais', to='plano.NotasAdicionais')),
            ],
            options={
                'verbose_name': 'Plano',
                'permissions': (('view_plano', 'Can view plano'),),
            },
        ),
        migrations.CreateModel(
            name='TipoPlano',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=32)),
                ('codigo', models.CharField(max_length=15)),
                ('valor_mensal', models.DecimalField(decimal_places=2, max_digits=12, validators=[django.core.validators.MinValueValidator(Decimal('0.00'))])),
                ('valor_anual', models.DecimalField(decimal_places=2, max_digits=12, validators=[django.core.validators.MinValueValidator(Decimal('0.00'))])),
            ],
        ),
        migrations.CreateModel(
            name='UsuariosAdicionais',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantidade', models.IntegerField(default=0)),
                ('valor', models.DecimalField(decimal_places=2, max_digits=12, validators=[django.core.validators.MinValueValidator(Decimal('0.00'))])),
            ],
        ),
        migrations.AddField(
            model_name='plano',
            name='tipo_plano',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='tipo_plano', to='plano.TipoPlano'),
        ),
        migrations.AddField(
            model_name='plano',
            name='usuarios_adicionais',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='usuarios_adicionais', to='plano.UsuariosAdicionais'),
        ),
        migrations.AddField(
            model_name='pagamentos',
            name='plano',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='pagamentos_plano', to='plano.Plano'),
        ),
    ]
