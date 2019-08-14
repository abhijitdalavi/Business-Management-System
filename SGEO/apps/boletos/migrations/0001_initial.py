# Generated by Django 2.0.5 on 2019-05-01 23:39

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Boleto',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('token', models.CharField(blank=True, max_length=255, null=True)),
                ('emissao', models.DateField()),
                ('vencimento', models.DateField()),
                ('documento', models.CharField(max_length=32)),
                ('numero', models.CharField(max_length=32)),
                ('titulo', models.CharField(max_length=32)),
                ('valor', models.DecimalField(decimal_places=2, max_digits=15)),
                ('status', models.CharField(choices=[('0', 'Em digitação'), ('1', 'Emitido')], max_length=2)),
            ],
        ),
        migrations.CreateModel(
            name='ConfiguracaoBoleto',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome_razao_social', models.CharField(max_length=255)),
                ('cpf_cnpj', models.CharField(max_length=32)),
                ('cep', models.CharField(max_length=9)),
                ('estado', models.CharField(choices=[('AC', 'AC'), ('AL', 'AL'), ('AP', 'AP'), ('AM', 'AM'), ('BA', 'BA'), ('CE', 'CE'), ('DF', 'DF'), ('ES', 'ES'), ('EX', 'EX'), ('GO', 'GO'), ('MA', 'MA'), ('MT', 'MT'), ('MS', 'MS'), ('MG', 'MG'), ('PA', 'PA'), ('PB', 'PB'), ('PR', 'PR'), ('PE', 'PE'), ('PI', 'PI'), ('RJ', 'RJ'), ('RN', 'RN'), ('RS', 'RS'), ('RO', 'RO'), ('RR', 'RR'), ('SC', 'SC'), ('SP', 'SP'), ('SE', 'SE'), ('TO', 'TO')], max_length=3)),
                ('cidade', models.CharField(max_length=255)),
                ('bairro', models.CharField(max_length=255)),
                ('logradouro', models.CharField(max_length=255)),
                ('numero', models.CharField(max_length=10)),
                ('complemento', models.CharField(blank=True, max_length=80, null=True)),
                ('instrucoes', models.CharField(blank=True, max_length=500, null=True)),
                ('carteira', models.CharField(max_length=6)),
                ('banco', models.CharField(choices=[('001', '001 - BANCO DO BRASIL S.A.'), ('004', '004 - BANCO DO NORDESTE DO BRASIL S.A.'), ('021', '021 - BANESTES S.A. BANCO DO ESTADO DO ESPIRITO SANTO'), ('033', '033 - BANCO SANTANDER (BRASIL) S.A.'), ('041', '041 - BANCO DO ESTADO DO RIO GRANDE DO SUL S.A.'), ('104', '104 - CAIXA ECONOMICA FEDERAL'), ('237', '237 - BANCO BRADESCO S.A.'), ('341', '341 - BANCO ITAÚ S.A.'), ('399', '399 - HSBC BANK BRASIL S.A. - BANCO MULTIPLO'), ('422', '422 - BANCO SAFRA S.A.'), ('748', '748 - BANCO COOPERATIVO SICREDI S.A.'), ('756', '756 - BANCO COOPERATIVO DO BRASIL S.A. - BANCOOB'), ('757', '757 - BANCO KEB DO BRASIL S.A.')], max_length=3)),
                ('agencia', models.CharField(max_length=8)),
                ('conta', models.CharField(max_length=32)),
                ('digito', models.CharField(max_length=8)),
            ],
        ),
    ]
