# Generated by Django 4.1.3 on 2022-12-01 18:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('factura', '0002_remove_factura_fecha_factura_fecha_l'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='factura',
            options={'ordering': ('-fecha',)},
        ),
        migrations.RenameField(
            model_name='facturadetalle',
            old_name='total',
            new_name='valor',
        ),
    ]
