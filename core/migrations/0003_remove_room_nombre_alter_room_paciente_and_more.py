# Generated by Django 5.1.1 on 2024-11-12 06:27

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_alter_institucion_tipo_institucion_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='room',
            name='nombre',
        ),
        migrations.AlterField(
            model_name='room',
            name='paciente',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='rooms_as_paciente', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='room',
            name='terapeuta',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='rooms_as_terapeuta', to=settings.AUTH_USER_MODEL),
        ),
    ]
