# Generated by Django 2.2.5 on 2019-10-29 05:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('movimientos', '0022_auto_20191009_2129'),
    ]

    operations = [
        migrations.AlterField(
            model_name='equipo_asignado',
            name='id_equipo',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='inventario.Equipo_for_asig', verbose_name='Equipo'),
        ),
    ]