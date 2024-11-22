# Generated by Django 5.1.1 on 2024-10-17 03:52

import django.contrib.auth.models
import django.contrib.auth.validators
import django.db.models.deletion
import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='Ciudad',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_ciudad', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='ContenidoTerapia',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=100)),
                ('url_contenido', models.URLField()),
                ('descripcion', models.TextField()),
                ('fecha_publicacion', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Pais',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_pais', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='TipoInstitucion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_tipo', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Comuna',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_comuna', models.CharField(max_length=100)),
                ('ciudad', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='core.ciudad')),
            ],
        ),
        migrations.CreateModel(
            name='Direccion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_direccion', models.CharField(max_length=100)),
                ('comuna', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='core.comuna')),
            ],
        ),
        migrations.CreateModel(
            name='Region',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_region', models.CharField(max_length=100)),
                ('pais', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='core.pais')),
            ],
        ),
        migrations.AddField(
            model_name='ciudad',
            name='region',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='core.region'),
        ),
        migrations.CreateModel(
            name='SesionTerapia',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha_sesion', models.DateTimeField()),
                ('duracion', models.PositiveIntegerField()),
                ('resultado', models.PositiveIntegerField(choices=[(1, 'Completa'), (2, 'Interrumpida')], default=0)),
                ('contenido', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.contenidoterapia')),
            ],
        ),
        migrations.CreateModel(
            name='Institucion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('contacto', models.CharField(max_length=100)),
                ('direccion', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='core.direccion')),
                ('tipo_institucion', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='core.tipoinstitucion')),
            ],
        ),
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='username')),
                ('first_name', models.CharField(blank=True, max_length=150, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('rut', models.CharField(max_length=12, unique=True)),
                ('fecha_registro', models.DateField(auto_now_add=True)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('rol', models.PositiveIntegerField(choices=[(1, 'Paciente'), (2, 'Terapeuta'), (3, 'Administrador'), (4, 'Cliente')])),
                ('estado_activo', models.BooleanField(default=True)),
                ('groups', models.ManyToManyField(blank=True, help_text='Grupo al que pertenece el usuario.', related_name='usuario_set', to='auth.group', verbose_name='grupos')),
                ('institucion', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='core.institucion')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Permisos específicos del usuario.', related_name='usuario_set', to='auth.permission', verbose_name='permisos de usuario')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='Suscripcion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha_inicio', models.DateField()),
                ('fecha_fin', models.DateField()),
                ('estado_activo', models.BooleanField(default=True)),
                ('usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.usuario')),
            ],
        ),
        migrations.CreateModel(
            name='SignosVitales',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('frecuencia_cardiaca', models.PositiveIntegerField()),
                ('fecha_medicion', models.DateTimeField()),
                ('hora_medicion', models.TimeField()),
                ('sesion', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.sesionterapia')),
                ('usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.usuario')),
            ],
        ),
        migrations.CreateModel(
            name='UsuarioSesion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rol', models.PositiveIntegerField(choices=[(1, 'Paciente'), (2, 'Terapeuta'), (3, 'Administrador'), (4, 'Cliente')])),
                ('sesion', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.sesionterapia')),
                ('usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.usuario')),
            ],
        ),
        migrations.AddField(
            model_name='sesionterapia',
            name='usuario',
            field=models.ManyToManyField(through='core.UsuarioSesion', to='core.usuario'),
        ),
    ]
