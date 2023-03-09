from django.db import models

# Create your models here.


class Departamento(models.Model):

    aNombre = models.CharField("aNombre", max_length=50)
    aNombreCorto = models.CharField("aNombreCorto", max_length=5, unique=True)
    nActivo = models.BooleanField("nActivo", default=False)

    class Meta:
        verbose_name = 'Department'  # Alias
        verbose_name_plural = 'Departments'  # Alias plural
        ordering = ['-aNombre']  # ordenacion
        unique_together = (
            'aNombre',
            'aNombreCorto'
        )  # Registro unico

    def __str__(self):
        return str(self.id) + ' - ' + self.aNombre + ' - ' + self.aNombreCorto + ' - ' + str(self.nActivo)
