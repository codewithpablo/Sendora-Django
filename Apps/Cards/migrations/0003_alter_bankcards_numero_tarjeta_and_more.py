# Generated by Django 5.1.3 on 2024-11-18 15:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Cards', '0002_alter_bankcards_options_alter_senodoracards_options'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bankcards',
            name='numero_tarjeta',
            field=models.CharField(max_length=19, unique=True),
        ),
        migrations.AlterField(
            model_name='senodoracards',
            name='numero_tarjeta',
            field=models.CharField(max_length=19, unique=True),
        ),
    ]
