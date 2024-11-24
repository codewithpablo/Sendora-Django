# Generated by Django 5.1.3 on 2024-11-20 20:22

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Accounts', '0014_alter_bankaccounts_saldo'),
        ('Transactions', '0005_alter_transactions_motivo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='transactions',
            name='destinatario',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='transaciones_como_destinatario', to='Accounts.sendoraaccounts'),
        ),
        migrations.AlterField(
            model_name='transactions',
            name='remitente',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='transaciones_como_remitente', to='Accounts.sendoraaccounts'),
        ),
    ]