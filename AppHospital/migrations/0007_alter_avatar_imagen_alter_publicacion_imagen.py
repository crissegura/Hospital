# Generated by Django 4.1 on 2022-09-28 16:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AppHospital', '0006_alter_publicacion_autor_alter_publicacion_fecha_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='avatar',
            name='imagen',
            field=models.ImageField(blank=True, null=True, upload_to='avatars'),
        ),
        migrations.AlterField(
            model_name='publicacion',
            name='imagen',
            field=models.ImageField(blank=True, null=True, upload_to='photos'),
        ),
    ]
