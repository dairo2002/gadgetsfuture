# Generated by Django 5.0.1 on 2024-01-31 15:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cuenta', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='cuenta',
            old_name='personal',
            new_name='is_staff',
        ),
    ]