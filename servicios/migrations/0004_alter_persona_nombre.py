# Generated by Django 4.1.1 on 2022-09-30 01:17

from django.db import migrations, models
import servicios.validators


class Migration(migrations.Migration):

    dependencies = [
        ('servicios', '0003_usuario_correo_usuario_unidades_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='persona',
            name='nombre',
            field=models.CharField(max_length=100, validators=[servicios.validators.validar_caracteres_especiales]),
        ),
    ]