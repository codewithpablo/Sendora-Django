# Generated by Django 5.1.3 on 2024-11-13 21:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Users', '0002_alter_users_dni'),
    ]

    operations = [
        migrations.AlterField(
            model_name='users',
            name='photo',
            field=models.ImageField(default='users/no-photo.jpg', null=True, upload_to='users/', verbose_name='Foto de perfil'),
        ),
    ]