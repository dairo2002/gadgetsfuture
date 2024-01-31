# Generated by Django 5.0.1 on 2024-01-31 04:19

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cuenta',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('nombre', models.CharField(max_length=50)),
                ('apellido', models.CharField(max_length=50)),
                ('usuario', models.CharField(max_length=50, unique=True)),
                ('correo_electronico', models.EmailField(max_length=100, unique=True)),
                ('telefono', models.CharField(max_length=50)),
                ('inicio_acceso', models.DateField(auto_now_add=True)),
                ('ultimo_acceso', models.DateField(auto_now_add=True)),
                ('administrador', models.BooleanField(default=False)),
                ('personal', models.BooleanField(default=False)),
                ('activo', models.BooleanField(default=True)),
                ('super_administrador', models.BooleanField(default=False)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
