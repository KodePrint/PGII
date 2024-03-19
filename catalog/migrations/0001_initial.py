# Generated by Django 5.0.3 on 2024-03-17 01:15

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Equipment',
            fields=[
                ('basemodel_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='core.basemodel')),
                ('name', models.CharField(max_length=100, verbose_name='nombre')),
                ('description', models.TextField(verbose_name='description')),
                ('img', models.ImageField(upload_to='', verbose_name='image')),
            ],
            options={
                'verbose_name': 'Equipment',
                'verbose_name_plural': 'Equipments',
            },
            bases=('core.basemodel',),
        ),
        migrations.CreateModel(
            name='Material',
            fields=[
                ('basemodel_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='core.basemodel')),
                ('name', models.CharField(max_length=100, verbose_name='nombre')),
                ('description', models.TextField(verbose_name='description')),
                ('img', models.ImageField(upload_to='', verbose_name='image')),
            ],
            options={
                'verbose_name': 'Material',
                'verbose_name_plural': 'Materials',
            },
            bases=('core.basemodel',),
        ),
    ]