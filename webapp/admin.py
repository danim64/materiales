from django.contrib import admin
from .models import Materiales, Grupo, Marca, Proveedor, Unidad

admin.site.register(Materiales)
admin.site.register(Grupo)
admin.site.register(Marca)
admin.site.register(Proveedor)
admin.site.register(Unidad)
