# django
from django.db import models

# modelos 
from .computer import Computadora

class Orden(models.Model):
  computadoras = models.ManyToManyField(Computadora, related_name='computadoras')
  contadorOrdenes = models.IntegerField()
  total_costo = models.IntegerField(null=True, blank=True)
  fecha = models.DateTimeField(auto_now_add=True)
