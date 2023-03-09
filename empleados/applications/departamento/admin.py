from django.contrib import admin

# Importo la clase del modelo
from .models import Departamento

# Register your models here.
## Es lo necesario para imporar los modelos al daministrador
admin.site.register(Departamento)