# Generated by Django 5.0.1 on 2024-02-19 04:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tienda', '0005_alter_categoria_descuento'),
    ]

    operations = [
        migrations.AlterField(
            model_name='categoria',
            name='descuento',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]