# Generated by Django 5.1.1 on 2024-11-13 07:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
        ('core', '0004_alter_usuario_groups_alter_usuario_user_permissions'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usuario',
            name='groups',
            field=models.ManyToManyField(blank=True, help_text='Grupo al que pertenece el usuario.', related_name='usuario_set', to='auth.group', verbose_name='grupos'),
        ),
        migrations.AlterField(
            model_name='usuario',
            name='user_permissions',
            field=models.ManyToManyField(blank=True, help_text='Permisos específicos del usuario.', related_name='usuario_set', to='auth.permission', verbose_name='permisos de usuario'),
        ),
    ]
