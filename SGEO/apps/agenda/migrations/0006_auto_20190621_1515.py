# Generated by Django 2.0.5 on 2019-06-21 18:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('agenda', '0005_auto_20190621_1054'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='events',
            options={'permissions': (('view_events', 'Can view evento agenda'),), 'verbose_name': 'Evento na Agenda'},
        ),
    ]
