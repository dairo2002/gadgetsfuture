# Generated by Django 5.0.1 on 2024-02-19 04:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tienda', '0006_alter_categoria_descuento'),
    ]

    operations = [
        migrations.AlterField(
            model_name='categoria',
            name='descuento',
            field=models.FloatField(blank=True, null=True),
        ),
    ]