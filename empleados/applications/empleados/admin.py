from django.contrib import admin
from .models import *
# Register your models here.

"""MODIFICAR EL ADMIN"""
class EmpleadoAdmin(admin.ModelAdmin):
    list_display = (
        'aNombreEmpleado',
        'aApellidoEmpleado',
        'aTrabajo',
        'aDepartamento'
    )

""" Registrar la tabla de empleados"""
admin.site.register(Empleado, EmpleadoAdmin)
admin.site.register(Habilidades)


