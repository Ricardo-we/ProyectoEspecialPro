# Generated by Django 3.2.5 on 2021-08-28 02:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ProyectoEspecialApp', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='downloads',
            options={'verbose_name': 'Download', 'verbose_name_plural': 'Downloads'},
        ),
        migrations.AlterModelOptions(
            name='updates',
            options={'verbose_name': 'Update', 'verbose_name_plural': 'Updates'},
        ),
        migrations.AlterField(
            model_name='downloads',
            name='archivo',
            field=models.FileField(upload_to='descargas'),
        ),
    ]
