# Generated by Django 2.0.5 on 2019-05-05 18:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crm2', '0002_etiqueta'),
    ]

    operations = [
        migrations.AddField(
            model_name='oportunidade',
            name='etiquetas',
            field=models.ManyToManyField(blank=True, null=True, to='crm2.Etiqueta'),
        ),
    ]