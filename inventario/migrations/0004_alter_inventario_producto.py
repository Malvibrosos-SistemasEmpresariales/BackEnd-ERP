# Generated by Django 4.1.3 on 2022-11-28 00:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('producto', '0001_initial'),
        ('inventario', '0003_remove_inventario_id_alter_inventario_producto'),
    ]

    operations = [
        migrations.AlterField(
            model_name='inventario',
            name='producto',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='producto.producto', unique=True),
        ),
    ]
