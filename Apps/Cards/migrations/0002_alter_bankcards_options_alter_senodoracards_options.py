# Generated by Django 5.1.3 on 2024-11-17 17:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Cards', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='bankcards',
            options={'verbose_name': 'Bancaria', 'verbose_name_plural': 'Bancaria'},
        ),
        migrations.AlterModelOptions(
            name='senodoracards',
            options={'verbose_name': 'Sendora', 'verbose_name_plural': 'Sendora'},
        ),
    ]
