# Generated by Django 4.1.6 on 2023-03-09 04:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('departamento', '0003_alter_departamento_options_and_more'),
        ('empleados', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Habilidades',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('aHabilidad', models.CharField(max_length=50, verbose_name='aHabilidad')),
            ],
            options={
                'verbose_name': 'Ability',
                'verbose_name_plural': 'Abilities',
                'ordering': ['aHabilidad'],
            },
        ),
        migrations.AlterModelOptions(
            name='empleado',
            options={'ordering': ['aApellidoEmpleado', 'aNombreEmpleado'], 'verbose_name': 'Employee', 'verbose_name_plural': 'Employees'},
        ),
        migrations.AlterUniqueTogether(
            name='empleado',
            unique_together={('aNombreEmpleado', 'aApellidoEmpleado', 'aTrabajo', 'aDepartamento')},
        ),
    ]
