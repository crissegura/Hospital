# Generated by Django 4.1 on 2022-09-28 23:20

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('AppHospital', '0009_comentario_alter_publicacion_autor'),
    ]

    operations = [
        migrations.AddField(
            model_name='comentario',
            name='comentarista',
            field=models.ForeignKey(default='' , on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
    ]