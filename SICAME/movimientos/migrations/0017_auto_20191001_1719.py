# Generated by Django 2.2.5 on 2019-10-01 23:19

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('movimientos', '0016_material_devuelto_comentario'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='material_devuelto',
            name='comentario',
        ),
        migrations.AddField(
            model_name='devolucion',
            name='comentario',
            field=ckeditor.fields.RichTextField(default='S/C', help_text='Apmplie con un comentario en que se utilizaronlos materiales transformados', verbose_name='Comentario'),
        ),
    ]
