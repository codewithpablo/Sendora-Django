# Generated by Django 5.1.3 on 2024-11-19 17:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Profiles', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profiles',
            name='foto_perfil',
            field=models.ImageField(default='users/no-photo.png', null=True, upload_to='users/', verbose_name='Foto de perfil'),
        ),
    ]