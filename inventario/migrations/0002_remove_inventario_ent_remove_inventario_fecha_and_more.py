# Generated by Django 4.1.3 on 2022-11-28 00:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('inventario', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='inventario',
            name='ent',
        ),
        migrations.RemoveField(
            model_name='inventario',
            name='fecha',
        ),
        migrations.RemoveField(
            model_name='inventario',
            name='fin',
        ),
        migrations.RemoveField(
            model_name='inventario',
            name='ini',
        ),
        migrations.RemoveField(
            model_name='inventario',
            name='sal',
        ),
        migrations.AddField(
            model_name='inventario',
            name='cantidad',
            field=models.IntegerField(default=None),
            preserve_default=False,
        ),
        migrations.CreateModel(
            name='InventarioMovimientos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cantidad', models.IntegerField()),
                ('fecha', models.DateField()),
                ('inventario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='inventario.inventario')),
            ],
        ),
    ]