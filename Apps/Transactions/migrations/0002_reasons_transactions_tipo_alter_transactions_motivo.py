# Generated by Django 5.1.3 on 2024-11-15 16:51

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Transactions', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Reasons',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
            ],
        ),
        migrations.AddField(
            model_name='transactions',
            name='tipo',
            field=models.CharField(choices=[('entrada', 'Transferencia de entrada'), ('salida', 'Transferencia de salida')], max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='transactions',
            name='motivo',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Transactions.reasons'),
        ),
    ]
