# Generated by Django 2.0.5 on 2019-05-15 02:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fiscal', '0002_auto_20190508_1037'),
    ]

    operations = [
        migrations.AlterField(
            model_name='notafiscal',
            name='mod',
            field=models.CharField(choices=[('55', 'NF-e (55)'), ('65', 'NFC-e (65)')], default='55', max_length=2),
        ),
    ]
