# Generated by Django 4.1.3 on 2022-11-27 22:07

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Isla',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('centroComercial', models.CharField(max_length=50)),
                ('ciudad', models.CharField(max_length=50)),
            ],
        ),
    ]
