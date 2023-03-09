from django.db import models
from applications.departamento.models import Departamento

# Create your models here.


class Habilidades(models.Model):
    """MODELO PARA LAS HABILIDADES DE LOS EMPLEADOS"""
    aHabilidad = models.CharField('aHabilidad', max_length=50)

    class Meta:
        """MODIICACIONES A LA TABLA DEL ADMIN"""
        verbose_name = 'Ability'
        verbose_name_plural = 'Abilities'
        ordering = [
            'aHabilidad'
        ]
        
    
    def __str__(self):
        return str(self.id) + " - " + self.aHabilidad

class Empleado(models.Model):
    """ MODELO PARA LA TABLA DE EMPLEADOS """

    aTrabajo = (
        ('0', 'contador'),
        ('1', 'administrador'),
        ('2', 'economista'),
        ('4', 'otro'),
    )

    aNombreEmpleado = models.CharField("aNombreEmpleado", max_length=50)
    aApellidoEmpleado = models.CharField("aApellidoEmpleado", max_length=50)
    aTrabajo = models.CharField(
        "aDepeartamento", max_length=1, choices=aTrabajo)
    aDepartamento = models.ForeignKey(Departamento, on_delete=models.CASCADE)
    # fImage = models.ImageField(, upload_to=None, height_field=None, width_field=None, max_length=None)
    aHabilidades = models.ManyToManyField(Habilidades)

    class Meta:
        verbose_name = 'Employee'
        verbose_name_plural = 'Employees'
        ordering = [
            'aApellidoEmpleado',
            'aNombreEmpleado'
        ]
        unique_together = (
            'aNombreEmpleado',
            'aApellidoEmpleado',
            'aTrabajo',
            'aDepartamento'
        )

    def __str__(self):
        return str(self.id) + ' - ' + self.aNombreEmpleado + ' - ' + self.aApellidoEmpleado + ' - ' + self.aTrabajo + ' - ' + str(self.aDepartamento)
