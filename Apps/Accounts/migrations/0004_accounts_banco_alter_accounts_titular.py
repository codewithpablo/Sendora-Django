# Generated by Django 5.1.3 on 2024-11-15 17:32

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Accounts', '0003_remove_accounts_transacciones_alter_accounts_saldo'),
        ('Banks', '0002_alter_banks_options'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='accounts',
            name='banco',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='Banks.banks'),
        ),
        migrations.AlterField(
            model_name='accounts',
            name='titular',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
