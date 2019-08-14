# Generated by Django 2.0.5 on 2019-05-01 23:39

from decimal import Decimal
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import SGEO.apps.cadastro.models.empresa


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Banco',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('banco', models.CharField(blank=True, choices=[('001', '001 - BANCO DO BRASIL S.A.'), ('003', '003 - BANCO DA AMAZONIA S.A.'), ('004', '004 - BANCO DO NORDESTE DO BRASIL S.A.'), ('012', '012 - BANCO STANDARD DE INVESTIMENTOS S.A.'), ('014', '014 - NATIXIS BRASIL S.A. BANCO MÚLTIPLO'), ('019', '019 - BANCO AZTECA DO BRASIL S.A.'), ('021', '021 - BANESTES S.A. BANCO DO ESTADO DO ESPIRITO SANTO'), ('024', '024 - BANCO DE PERNAMBUCO S.A. - BANDEPE'), ('025', '025 - BANCO ALFA S.A.'), ('029', '029 - BANCO BANERJ S.A.'), ('031', '031 - BANCO BEG S.A.'), ('033', '033 - BANCO SANTANDER (BRASIL) S.A.'), ('036', '036 - BANCO BRADESCO BBI S.A.'), ('037', '037 - BANCO DO ESTADO DO PARÁ S.A.'), ('040', '040 - BANCO CARGILL S.A.'), ('041', '041 - BANCO DO ESTADO DO RIO GRANDE DO SUL S.A.'), ('044', '044 - BANCO BVA S.A.'), ('045', '045 - BANCO OPPORTUNITY S.A.'), ('047', '047 - BANCO DO ESTADO DE SERGIPE S.A.'), ('062', '062 - HIPERCARD BANCO MÚLTIPLO S.A.'), ('063', '063 - BANCO IBI S.A. - BANCO MÚLTIPLO'), ('065', '065 - BANCO LEMON S.A.'), ('066', '066 - BANCO MORGAN STANLEY S.A.'), ('069', '069 - BPN BRASIL BANCO MÚLTIPLO S.A.'), ('070', '070 - BRB - BANCO DE BRASILIA S.A.'), ('072', '072 - BANCO RURAL MAIS S.A.'), ('073', '073 - BB BANCO POPULAR DO BRASIL S.A.'), ('074', '074 - BANCO J. SAFRA S.A.'), ('075', '075 - BANCO CR2 S/A'), ('076', '076 - BANCO KDB DO BRASIL S.A.'), ('077', '077 - BANCO INTERMEDIUM S/A'), ('078', '078 - BES INVESTIMENTO DO BRASIL S.A. - BANCO DE INVESTIMENTO'), ('079', '079 - JBS BANCO S/A'), ('081', '081 - CONCÓRDIA BANCO S.A.'), ('082', '082 - BANCO TOPÁZIO S.A.'), ('083', '083 - BANCO DA CHINA BRASIL S.A'), ('096', '096 - BANCO BM&F DE SERVIÇOS DE LIQUIDAÇÃO E CUSTÓDIA S.A.'), ('104', '104 - CAIXA ECONOMICA FEDERAL'), ('107', '107 - BANCO BBM S/A'), ('151', '151 - BANCO NOSSA CAIXA S.A.'), ('184', '184 - BANCO ITAÚ BBA S.A.'), ('204', '204 - BANCO BRADESCO CARTÕES S.A.'), ('208', '208 - BANCO UBS PACTUAL S.A.'), ('212', '212 - BANCO MATONE S.A.'), ('213', '213 - BANCO ARBI S.A.'), ('214', '214 - BANCO DIBENS S.A.'), ('215', '215 - BANCO COMERCIAL E DE INVESTIMENTO SUDAMERIS S.A.'), ('217', '217 - BANCO JOHN DEERE S.A.'), ('218', '218 - BANCO BONSUCESSO S.A.'), ('222', '222 - BANCO CALYON BRASIL S.A.'), ('224', '224 - BANCO FIBRA S.A.'), ('225', '225 - BANCO BRASCAN S.A.'), ('229', '229 - BANCO CRUZEIRO DO SUL S.A.'), ('230', '230 - UNICARD BANCO MÚLTIPLO S.A.'), ('233', '233 - BANCO GE CAPITAL S.A.'), ('237', '237 - BANCO BRADESCO S.A.'), ('241', '241 - BANCO CLASSICO S.A.'), ('243', '243 - BANCO MÁXIMA S.A.'), ('246', '246 - BANCO ABC BRASIL S.A.'), ('248', '248 - BANCO BOAVISTA INTERATLANTICO S.A.'), ('249', '249 - BANCO INVESTCRED UNIBANCO S.A.'), ('250', '250 - BANCO SCHAHIN S.A.'), ('254', '254 - PARANÁ BANCO S.A.'), ('263', '263 - BANCO CACIQUE S.A.'), ('265', '265 - BANCO FATOR S.A.'), ('266', '266 - BANCO CEDULA S.A.'), ('300', '300 - BANCO DE LA NACION ARGENTINA'), ('318', '318 - BANCO BMG S.A.'), ('320', '320 - BANCO INDUSTRIAL E COMERCIAL S.A.'), ('341', '341 - BANCO ITAÚ S.A.'), ('366', '366 - BANCO SOCIETE GENERALE BRASIL S.A.'), ('370', '370 - BANCO WESTLB DO BRASIL S.A.'), ('376', '376 - BANCO J.P. MORGAN S.A.'), ('389', '389 - BANCO MERCANTIL DO BRASIL S.A.'), ('394', '394 - BANCO FINASA BMC S.A.'), ('399', '399 - HSBC BANK BRASIL S.A. - BANCO MULTIPLO'), ('409', '409 - UNIBANCO-UNIAO DE BANCOS BRASILEIROS S.A.'), ('412', '412 - BANCO CAPITAL S.A.'), ('422', '422 - BANCO SAFRA S.A.'), ('453', '453 - BANCO RURAL S.A.'), ('456', '456 - BANCO DE TOKYO-MITSUBISHI UFJ BRASIL S/A'), ('464', '464 - BANCO SUMITOMO MITSUI BRASILEIRO S.A.'), ('473', '473 - BANCO CAIXA GERAL - BRASIL S.A.'), ('477', '477 - CITIBANK N.A.'), ('479', '479 - BANCO ITAUBANK S.A.'), ('487', '487 - DEUTSCHE BANK S.A. - BANCO ALEMAO'), ('488', '488 - JPMORGAN CHASE BANK, NATIONAL ASSOCIATION'), ('492', '492 - ING BANK N.V.'), ('494', '494 - BANCO DE LA REPUBLICA ORIENTAL DEL URUGUAY'), ('495', '495 - BANCO DE LA PROVINCIA DE BUENOS AIRES'), ('505', '505 - BANCO CREDIT SUISSE (BRASIL) S.A.'), ('600', '600 - BANCO LUSO BRASILEIRO S.A.'), ('604', '604 - BANCO INDUSTRIAL DO BRASIL S.A.'), ('610', '610 - BANCO VR S.A.'), ('611', '611 - BANCO PAULISTA S.A.'), ('612', '612 - BANCO GUANABARA S.A.'), ('613', '613 - BANCO PECUNIA S.A.'), ('623', '623 - BANCO PANAMERICANO S.A.'), ('626', '626 - BANCO FICSA S.A.'), ('630', '630 - BANCO INTERCAP S.A.'), ('633', '633 - BANCO RENDIMENTO S.A.'), ('634', '634 - BANCO TRIANGULO S.A.'), ('637', '637 - BANCO SOFISA S.A.'), ('638', '638 - BANCO PROSPER S.A.'), ('641', '641 - BANCO ALVORADA S.A.'), ('643', '643 - BANCO PINE S.A.'), ('652', '652 - ITAÚ UNIBANCO BANCO MÚLTIPLO S.A.'), ('653', '653 - BANCO INDUSVAL S.A.'), ('654', '654 - BANCO A.J. RENNER S.A.'), ('655', '655 - BANCO VOTORANTIM S.A.'), ('707', '707 - BANCO DAYCOVAL S.A.'), ('719', '719 - BANIF - BANCO INTERNACIONAL DO FUNCHAL (BRASIL), S.A.'), ('721', '721 - BANCO CREDIBEL S.A.'), ('734', '734 - BANCO GERDAU S.A'), ('735', '735 - BANCO POTTENCIAL S.A.'), ('738', '738 - BANCO MORADA S.A'), ('739', '739 - BANCO BGN S.A.'), ('740', '740 - BANCO BARCLAYS S.A.'), ('741', '741 - BANCO RIBEIRAO PRETO S.A.'), ('743', '743 - BANCO SEMEAR S.A.'), ('745', '745 - BANCO CITIBANK S.A.'), ('746', '746 - BANCO MODAL S.A.'), ('747', '747 - BANCO RABOBANK INTERNATIONAL BRASIL S.A.'), ('748', '748 - BANCO COOPERATIVO SICREDI S.A.'), ('749', '749 - BANCO SIMPLES S.A.'), ('751', '751 - DRESDNER BANK BRASIL S.A. BANCO MULTIPLO'), ('752', '752 - BANCO BNP PARIBAS BRASIL S.A.'), ('753', '753 - NBC BANK BRASIL S. A. - BANCO MÚLTIPLO'), ('756', '756 - BANCO COOPERATIVO DO BRASIL S.A. - BANCOOB'), ('757', '757 - BANCO KEB DO BRASIL S.A.')], max_length=3, null=True)),
                ('agencia', models.CharField(blank=True, max_length=8, null=True)),
                ('conta', models.CharField(blank=True, max_length=32, null=True)),
                ('digito', models.CharField(blank=True, max_length=8, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Categoria',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('categoria_desc', models.CharField(max_length=32)),
            ],
            options={
                'verbose_name': 'Categoria',
                'permissions': (('view_categoria', 'Can view categoria'),),
            },
        ),
        migrations.CreateModel(
            name='Documento',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tipo', models.CharField(max_length=32)),
                ('documento', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Email',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Endereco',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tipo_endereco', models.CharField(blank=True, choices=[('UNI', 'Único'), ('RES', 'Residencial'), ('COM', 'Comercial'), ('COB', 'Cobrança'), ('ENT', 'Entrega'), ('OUT', 'Outro')], max_length=3, null=True)),
                ('logradouro', models.CharField(blank=True, max_length=255, null=True)),
                ('numero', models.CharField(blank=True, max_length=16, null=True)),
                ('bairro', models.CharField(blank=True, max_length=64, null=True)),
                ('complemento', models.CharField(blank=True, max_length=64, null=True)),
                ('pais', models.CharField(blank=True, default='Brasil', max_length=32, null=True)),
                ('cpais', models.CharField(blank=True, default='1058', max_length=5, null=True)),
                ('municipio', models.CharField(blank=True, max_length=64, null=True)),
                ('cmun', models.CharField(blank=True, max_length=9, null=True)),
                ('cep', models.CharField(blank=True, max_length=16, null=True)),
                ('uf', models.CharField(blank=True, choices=[('AC', 'AC'), ('AL', 'AL'), ('AP', 'AP'), ('AM', 'AM'), ('BA', 'BA'), ('CE', 'CE'), ('DF', 'DF'), ('ES', 'ES'), ('EX', 'EX'), ('GO', 'GO'), ('MA', 'MA'), ('MT', 'MT'), ('MS', 'MS'), ('MG', 'MG'), ('PA', 'PA'), ('PB', 'PB'), ('PR', 'PR'), ('PE', 'PE'), ('PI', 'PI'), ('RJ', 'RJ'), ('RN', 'RN'), ('RS', 'RS'), ('RO', 'RO'), ('RR', 'RR'), ('SC', 'SC'), ('SP', 'SP'), ('SE', 'SE'), ('TO', 'TO')], max_length=3, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Grupo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('grupo_desc', models.CharField(max_length=32)),
            ],
            options={
                'verbose_name': 'Grupo',
                'permissions': (('view_grupo', 'Can view grupo'),),
            },
        ),
        migrations.CreateModel(
            name='Marca',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('marca_desc', models.CharField(max_length=32)),
            ],
            options={
                'verbose_name': 'Marca',
                'permissions': (('view_marca', 'Can view marca'),),
            },
        ),
        migrations.CreateModel(
            name='MinhaEmpresa',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='Pessoa',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome_razao_social', models.CharField(max_length=255)),
                ('tipo_pessoa', models.CharField(choices=[('PF', 'Pessoa Física'), ('PJ', 'Pessoa Jurídica')], max_length=2)),
                ('inscricao_municipal', models.CharField(blank=True, max_length=32, null=True)),
                ('informacoes_adicionais', models.CharField(blank=True, max_length=1055, null=True)),
                ('status_ativo', models.BooleanField(default=True)),
                ('data_criacao', models.DateTimeField(editable=False)),
                ('data_edicao', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='Produto',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('codigo', models.CharField(max_length=15)),
                ('codigo_barras', models.CharField(blank=True, max_length=16, null=True)),
                ('descricao', models.CharField(max_length=255)),
                ('modelo', models.CharField(blank=True, max_length=255, null=True)),
                ('genero', models.CharField(choices=[('00', 'Mercadoria para revenda'), ('01', 'Matéria-prima'), ('02', 'Embalagem'), ('03', 'Produto em processo'), ('04', 'Produto acabado'), ('05', 'Subproduto'), ('06', 'Produto Intermediário'), ('07', 'Material de uso e consumo'), ('08', 'Ativo Imobilizado'), ('09', 'Serviços'), ('10', 'Outros insumos'), ('99', 'Outros')], default='00', max_length=2)),
                ('producao', models.CharField(choices=[('0', 'Própria'), ('1', 'Terceiros')], default='1', max_length=1)),
                ('custo', models.DecimalField(decimal_places=2, default=Decimal('0.00'), max_digits=16, validators=[django.core.validators.MinValueValidator(Decimal('0.00'))])),
                ('venda', models.DecimalField(decimal_places=2, default=Decimal('0.00'), max_digits=16, validators=[django.core.validators.MinValueValidator(Decimal('0.00'))])),
                ('inf_adicionais', models.CharField(blank=True, max_length=255, null=True)),
                ('ncm', models.CharField(blank=True, max_length=11, null=True)),
                ('isbn', models.CharField(blank=True, max_length=11, null=True)),
                ('eangtin', models.CharField(blank=True, max_length=11, null=True)),
                ('origem', models.CharField(choices=[('0', '0 - Nacional'), ('1', '1 - Estrangeira - Importação direta.'), ('2', '2 - Estrangeira - Adquirida no mercado interno.'), ('3', '3 - Nacional - Mercadoria ou bem com Conteúdo de Importação superior a 40% e inferior ou igual a 70%.'), ('4', '4 - Nacional - Cuja produção tenha sido feita em conformidade com os processos produtivos básicos de que tratam o Decreto-Lei nº 288/67, e as Leis nºs 8.248/91, 8.387/91, 10.176/01 e 11.484/ 07'), ('5', '5 - Nacional - Mercadoria ou bem com Conteúdo de Importação inferior ou igual a 40% (quarenta por cento)'), ('6', '6 - Estrangeira - Importação direta, sem similar nacional, constante em lista da Resolução CAMEX nº 79/2012 e gás natural'), ('7', '7 - Estrangeira - Adquirida no mercado interno, sem similar nacional, constante em lista da Resolução CAMEX nº 79/2012 e gás natural'), ('8', '8 - Nacional - Mercadoria ou bem com Conteúdo de Importação superior a 70% (setenta por cento).')], default='0', max_length=1)),
                ('cest', models.CharField(blank=True, max_length=7, null=True)),
                ('depreciacao', models.DecimalField(decimal_places=2, default=Decimal('0.00'), max_digits=16, validators=[django.core.validators.MinValueValidator(Decimal('0.00'))])),
                ('estoque_minimo', models.DecimalField(decimal_places=2, default=Decimal('0.00'), max_digits=16, validators=[django.core.validators.MinValueValidator(Decimal('0.00'))])),
                ('estoque_atual', models.DecimalField(decimal_places=2, default=Decimal('0.00'), max_digits=16, validators=[django.core.validators.MinValueValidator(Decimal('0.00'))])),
                ('controlar_estoque', models.BooleanField(default=True)),
                ('status_ativo', models.BooleanField(default=True)),
                ('peso_liquido', models.DecimalField(decimal_places=2, default=Decimal('0.00'), max_digits=16, validators=[django.core.validators.MinValueValidator(Decimal('0.00'))])),
                ('peso_bruto', models.DecimalField(decimal_places=2, default=Decimal('0.00'), max_digits=16, validators=[django.core.validators.MinValueValidator(Decimal('0.00'))])),
                ('volumes', models.PositiveIntegerField(default=0)),
                ('itens_por_caixa', models.PositiveIntegerField(default=0)),
                ('altura', models.DecimalField(decimal_places=2, default=Decimal('0.00'), max_digits=16, validators=[django.core.validators.MinValueValidator(Decimal('0.00'))])),
                ('largura', models.DecimalField(decimal_places=2, default=Decimal('0.00'), max_digits=16, validators=[django.core.validators.MinValueValidator(Decimal('0.00'))])),
                ('profundidade', models.DecimalField(decimal_places=2, default=Decimal('0.00'), max_digits=16, validators=[django.core.validators.MinValueValidator(Decimal('0.00'))])),
                ('unidade_de_medida', models.CharField(choices=[('0', 'm'), ('1', 'cm'), ('2', 'mm')], default='1', max_length=1)),
                ('peso_com_embalagem', models.DecimalField(decimal_places=2, default=Decimal('0.00'), max_digits=16, validators=[django.core.validators.MinValueValidator(Decimal('0.00'))])),
                ('altura_com_embalagem', models.DecimalField(decimal_places=2, default=Decimal('0.00'), max_digits=16, validators=[django.core.validators.MinValueValidator(Decimal('0.00'))])),
                ('largura_com_embalagem', models.DecimalField(decimal_places=2, default=Decimal('0.00'), max_digits=16, validators=[django.core.validators.MinValueValidator(Decimal('0.00'))])),
                ('profundidade_com_embalagem', models.DecimalField(decimal_places=2, default=Decimal('0.00'), max_digits=16, validators=[django.core.validators.MinValueValidator(Decimal('0.00'))])),
                ('categoria', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='cadastro.Categoria')),
            ],
            options={
                'verbose_name': 'Produto',
                'permissions': (('view_produto', 'Can view produto'),),
            },
        ),
        migrations.CreateModel(
            name='Servico',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('codigo', models.CharField(max_length=15)),
                ('descricao', models.CharField(max_length=255)),
                ('tipo', models.CharField(choices=[('0', 'Prestado'), ('1', 'Tomado'), ('2', 'Prestado e Tomado')], default='0', max_length=1)),
                ('valor_venda', models.DecimalField(decimal_places=2, default=Decimal('0.00'), max_digits=16, validators=[django.core.validators.MinValueValidator(Decimal('0.00'))])),
                ('valor_custo', models.DecimalField(decimal_places=2, default=Decimal('0.00'), max_digits=16, validators=[django.core.validators.MinValueValidator(Decimal('0.00'))])),
                ('inf_adicionais', models.CharField(blank=True, max_length=255, null=True)),
                ('nbs', models.CharField(blank=True, max_length=15, null=True)),
                ('codigo_tributacao_municipal', models.CharField(blank=True, max_length=15, null=True)),
                ('codigo_municipal_servico', models.CharField(blank=True, max_length=15, null=True)),
                ('status_ativo', models.BooleanField(default=True)),
                ('categoria', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='cadastro.Categoria')),
            ],
        ),
        migrations.CreateModel(
            name='Site',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('site', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='StatusVenda',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status_venda', models.CharField(max_length=32)),
                ('posicao_navegacao', models.IntegerField(default=1)),
            ],
            options={
                'verbose_name': 'Status de Venda',
                'permissions': (('view_status_venda', 'Can view status_venda'),),
            },
        ),
        migrations.CreateModel(
            name='Telefone',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tipo_telefone', models.CharField(blank=True, choices=[('FIX', 'Fixo'), ('CEL', 'Celular'), ('FAX', 'Fax'), ('OUT', 'Outro')], max_length=8, null=True)),
                ('telefone', models.CharField(max_length=32)),
            ],
        ),
        migrations.CreateModel(
            name='Unidade',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sigla_unidade', models.CharField(max_length=3)),
                ('unidade_desc', models.CharField(max_length=16)),
            ],
            options={
                'verbose_name': 'Unidade',
                'permissions': (('view_unidade', 'Can view unidade'),),
            },
        ),
        migrations.CreateModel(
            name='Veiculo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descricao', models.CharField(max_length=255)),
                ('placa', models.CharField(blank=True, max_length=8, null=True)),
                ('uf', models.CharField(blank=True, choices=[('AC', 'AC'), ('AL', 'AL'), ('AP', 'AP'), ('AM', 'AM'), ('BA', 'BA'), ('CE', 'CE'), ('DF', 'DF'), ('ES', 'ES'), ('EX', 'EX'), ('GO', 'GO'), ('MA', 'MA'), ('MT', 'MT'), ('MS', 'MS'), ('MG', 'MG'), ('PA', 'PA'), ('PB', 'PB'), ('PR', 'PR'), ('PE', 'PE'), ('PI', 'PI'), ('RJ', 'RJ'), ('RN', 'RN'), ('RS', 'RS'), ('RO', 'RO'), ('RR', 'RR'), ('SC', 'SC'), ('SP', 'SP'), ('SE', 'SE'), ('TO', 'TO')], max_length=3, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('pessoa_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='cadastro.Pessoa')),
                ('limite_de_credito', models.DecimalField(blank=True, decimal_places=2, default=Decimal('0.00'), max_digits=15, null=True)),
                ('limite_restante', models.DecimalField(blank=True, decimal_places=2, default=Decimal('0.00'), max_digits=15, null=True)),
                ('indicador_ie', models.CharField(choices=[('1', 'Contribuinte ICMS'), ('2', 'Contribuinte isento de Inscrição'), ('9', 'Não Contribuinte')], default='9', max_length=1)),
                ('id_estrangeiro', models.CharField(blank=True, max_length=20, null=True)),
                ('comissao_vendedor', models.DecimalField(blank=True, decimal_places=2, default=Decimal('0.00'), max_digits=15, null=True)),
                ('proxima_visita', models.DateField(blank=True, null=True)),
            ],
            options={
                'verbose_name': 'Cliente',
                'permissions': (('view_cliente', 'Can view cliente'),),
            },
            bases=('cadastro.pessoa',),
        ),
        migrations.CreateModel(
            name='Empresa',
            fields=[
                ('pessoa_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='cadastro.Pessoa')),
                ('logo_file', models.ImageField(blank=True, default='imagens/logo.png', null=True, upload_to=SGEO.apps.cadastro.models.empresa.logo_directory_path)),
                ('cnae', models.CharField(blank=True, max_length=10, null=True)),
                ('iest', models.CharField(blank=True, max_length=32, null=True)),
            ],
            options={
                'verbose_name': 'Empresa',
                'permissions': (('view_empresa', 'Can view empresa'),),
            },
            bases=('cadastro.pessoa',),
        ),
        migrations.CreateModel(
            name='Fornecedor',
            fields=[
                ('pessoa_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='cadastro.Pessoa')),
                ('ramo', models.CharField(blank=True, max_length=64, null=True)),
            ],
            options={
                'verbose_name': 'Fornecedor',
                'permissions': (('view_fornecedor', 'Can view fornecedor'),),
            },
            bases=('cadastro.pessoa',),
        ),
        migrations.CreateModel(
            name='PessoaFisica',
            fields=[
                ('pessoa_id', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, related_name='pessoa_fis_info', serialize=False, to='cadastro.Pessoa')),
                ('cpf', models.CharField(blank=True, max_length=32, null=True)),
                ('rg', models.CharField(blank=True, max_length=32, null=True)),
                ('nascimento', models.DateField(blank=True, null=True)),
                ('sexo', models.CharField(blank=True, choices=[('M', 'Masculino'), ('F', 'Feminino'), ('O', 'Outro')], max_length=2, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='PessoaJuridica',
            fields=[
                ('pessoa_id', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, related_name='pessoa_jur_info', serialize=False, to='cadastro.Pessoa')),
                ('cnpj', models.CharField(blank=True, max_length=32, null=True)),
                ('nome_fantasia', models.CharField(blank=True, max_length=255, null=True)),
                ('inscricao_estadual', models.CharField(blank=True, max_length=32, null=True)),
                ('responsavel', models.CharField(blank=True, max_length=32, null=True)),
                ('sit_fiscal', models.CharField(blank=True, choices=[('LR', 'Lucro Real'), ('LP', 'Lucro Presumido'), ('SN', 'Simples Nacional'), ('SE', 'Simples Nacional, , excesso sublimite de receita bruta')], max_length=2, null=True)),
                ('suframa', models.CharField(blank=True, max_length=16, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Transportadora',
            fields=[
                ('pessoa_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='cadastro.Pessoa')),
            ],
            options={
                'verbose_name': 'Transportadora',
                'permissions': (('view_transportadora', 'Can view transportadora'),),
            },
            bases=('cadastro.pessoa',),
        ),
        migrations.CreateModel(
            name='Vendedor',
            fields=[
                ('pessoa_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='cadastro.Pessoa')),
                ('comissao_vendedor', models.DecimalField(blank=True, decimal_places=2, default=Decimal('0.00'), max_digits=15, null=True)),
                ('horas_trabalhadas_por_dia', models.DurationField(blank=True, null=True)),
                ('dias_folga_por_semana', models.PositiveIntegerField(blank=True, null=True)),
            ],
            options={
                'verbose_name': 'Vendedor',
                'permissions': (('view_vendedor', 'Can view vendedor'),),
            },
            bases=('cadastro.pessoa',),
        ),
        migrations.AddField(
            model_name='telefone',
            name='pessoa_tel',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='telefone', to='cadastro.Pessoa'),
        ),
        migrations.AddField(
            model_name='site',
            name='pessoa_site',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='site', to='cadastro.Pessoa'),
        ),
    ]
