# Generated by Django 5.1.3 on 2024-11-17 06:05

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Accounts', '0005_alter_accounts_titular'),
        ('Banks', '0002_alter_banks_options'),
    ]

    operations = [
        migrations.AlterField(
            model_name='accounts',
            name='banco',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='Banks.banks', unique=True),
        ),
    ]
