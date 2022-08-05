from django.contrib import admin

from app_orden.models import Orden, Seguimiento, SeguimientoAvance, SeguimientoArchivos

# Register your models here.
admin.site.register(Orden)
admin.site.register(Seguimiento)
admin.site.register(SeguimientoAvance)
admin.site.register(SeguimientoArchivos)