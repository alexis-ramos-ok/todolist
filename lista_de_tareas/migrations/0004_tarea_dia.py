# Generated by Django 4.2.2 on 2023-06-25 20:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lista_de_tareas', '0003_alter_tarea_descripcion'),
    ]

    operations = [
        migrations.AddField(
            model_name='tarea',
            name='dia',
            field=models.IntegerField(choices=[(1, 'Lunes'), (2, 'Martes'), (3, 'Miércoles'), (4, 'Jueves'), (5, 'Viernes'), (6, 'Sábado'), (7, 'Domingo')], default=1),
            preserve_default=False,
        ),
    ]