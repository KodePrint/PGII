# Generated by Django 2.2.5 on 2019-09-22 05:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('movimientos', '0007_auto_20190921_2229'),
    ]

    operations = [
        migrations.CreateModel(
            name='Recepccion',
            fields=[
            ],
            options={
                'verbose_name': 'Recepccion',
                'verbose_name_plural': 'Recepcciones',
                'proxy': True,
                'indexes': [],
                'constraints': [],
            },
            bases=('movimientos.devolucion',),
        ),
    ]