# Generated by Django 2.2.5 on 2019-09-14 02:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('asignacion', '0007_auto_20190913_1946'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='material_asig',
            name='modulo',
        ),
        migrations.AddField(
            model_name='material_asig',
            name='ubicacion',
            field=models.CharField(help_text='Debo de corregir y anclar bien la ubicacion', max_length=75, null=True, verbose_name='Ubicacion'),
        ),
    ]
