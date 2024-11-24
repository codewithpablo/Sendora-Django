# Generated by Django 5.1.3 on 2024-11-17 17:42

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Accounts', '0009_alter_bankaccounts_options_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='BankCards',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('numero_tarjeta', models.CharField(max_length=19)),
                ('fecha_expiracion', models.DateField()),
                ('cvv', models.CharField(max_length=4)),
                ('cuenta', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='Accounts.bankaccounts')),
            ],
        ),
        migrations.CreateModel(
            name='SenodoraCards',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('numero_tarjeta', models.CharField(max_length=19)),
                ('fecha_expiracion', models.DateField()),
                ('cvv', models.CharField(max_length=4)),
                ('cuenta', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='Accounts.sendoraaccounts')),
            ],
        ),
    ]
