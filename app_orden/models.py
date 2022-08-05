from django.db import models
from app_accounts.models import Account

class Orden(models.Model):
    
    nombre = models.CharField(max_length=50, unique=True)
    descripcion = models.CharField(max_length=255, blank=True)
    activo = models.BooleanField(default=True)  #1- ACTIVO 0-ANULADO
    prioridad =  models.BooleanField(default=False)
    estado = models.BooleanField(default=True) #1- ABIERTO 0-CERRADO
    fecha_creacion = models.DateTimeField(auto_now_add= True)

    class Meta():
        verbose_name = 'orden'
        verbose_name_plural = 'ordenes'

    def __str__(self):
        return self.nombre

class Seguimiento(models.Model):

    class status(models.IntegerChoices):
        ASIGNADO = 1
        TOMADO = 2
        TERMINADO = 3

    id_orden = models.ForeignKey(Orden,on_delete=models.CASCADE)    
    id_usuario_asignado = models.ForeignKey(Account, on_delete = models.CASCADE)
    nombre = models.CharField(max_length=50)
    status = models.IntegerField(choices=status.choices)
    cant_dias_proy = models.IntegerField()
    fecha_creacion = models.DateTimeField(auto_now_add=True)

class SeguimientoAvance(models.Model):
    id_seguimiento = models.ForeignKey(Seguimiento,on_delete=models.CASCADE)  
    nombre = models.CharField(max_length=50)
    descripcion = models.CharField(max_length=255, blank=True)
    fecha_creacion = models.DateTimeField(auto_now_add= True)

class SeguimientoArchivos(models.Model):
    id_seguimiento = models.ForeignKey(Seguimiento,on_delete=models.CASCADE)  
    nombre_path = models.CharField(max_length=70)
    nombre_real = models.CharField(max_length=30)
    fecha_creacion = models.DateTimeField(auto_now_add= True)
