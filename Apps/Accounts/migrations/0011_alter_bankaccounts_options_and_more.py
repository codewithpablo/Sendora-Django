# Generated by Django 5.1.3 on 2024-11-17 18:15

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Accounts', '0010_alter_bankaccounts_banco_alter_sendoraaccounts_banco'),
        ('Banks', '0002_alter_banks_options'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='bankaccounts',
            options={'verbose_name': 'Bancaria', 'verbose_name_plural': 'Bancarias'},
        ),
        migrations.AlterModelOptions(
            name='sendoraaccounts',
            options={'verbose_name': 'Sendora', 'verbose_name_plural': 'Sendora'},
        ),
        migrations.CreateModel(
            name='CorporateAccounts',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('alias', models.CharField(max_length=50)),
                ('saldo', models.IntegerField(default=0)),
                ('banco', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='Banks.banks')),
                ('titular', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Corporativa',
                'verbose_name_plural': 'Corporativas',
            },
        ),
    ]
