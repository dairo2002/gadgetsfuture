# Generated by Django 5.0.1 on 2024-01-31 18:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cuenta', '0007_rename_first_name_cuenta_apellido_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='cuenta',
            old_name='username',
            new_name='usuario',
        ),
    ]