# Generated by Django 5.1.3 on 2024-11-17 18:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Accounts', '0011_alter_bankaccounts_options_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='sendoraaccounts',
            name='banco',
        ),
    ]
