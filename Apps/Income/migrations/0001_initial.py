# Generated by Django 5.1.3 on 2024-11-17 14:49

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Accounts', '0007_accounts_id_alter_accounts_alias'),
    ]

    operations = [
        migrations.CreateModel(
            name='Incomes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('monto', models.FloatField()),
                ('fecha', models.DateTimeField(auto_now_add=True)),
                ('remitente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Accounts.accounts')),
            ],
            options={
                'verbose_name': 'Ingreso',
                'verbose_name_plural': 'Ingresos',
            },
        ),
    ]
