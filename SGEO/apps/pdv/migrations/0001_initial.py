# Generated by Django 2.0.5 on 2019-08-10 23:43

from decimal import Decimal
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('cadastro', '0006_auto_20190702_2151'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProdutoPDV',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantidade', models.PositiveIntegerField(default=1)),
                ('valor_unit', models.DecimalField(decimal_places=2, max_digits=12, validators=[django.core.validators.MinValueValidator(Decimal('0.00'))])),
                ('produto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='produto_pdv', to='cadastro.Produto')),
            ],
        ),
    ]