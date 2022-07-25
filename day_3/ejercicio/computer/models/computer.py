# django 
from django.db import models
from django.db.models import F
from django.forms import ValidationError
# modelos de componente

from .component import Procesador, PlacaBase, Monitor, Altavoz, Teclado, Raton

"""Clase de computadora armada"""


class Computadora(models.Model):
  """Crear objetos de tipo computadora"""
  nombre = models.CharField(max_length=100)
  procesador = models.ForeignKey(Procesador, on_delete=models.CASCADE)
  placabase = models.ForeignKey(PlacaBase, on_delete=models.CASCADE)
  monitor = models.ForeignKey(Monitor, on_delete=models.CASCADE)
  altavoz = models.ForeignKey(Altavoz, on_delete=models.CASCADE)
  teclado = models.ForeignKey(Teclado, on_delete=models.CASCADE)
  raton = models.ForeignKey(Raton, on_delete=models.CASCADE)
  contadorComputadoras = models.IntegerField(default=1)
  total_costo = models.IntegerField(null=True, blank=True)
  fecha = models.DateTimeField(auto_now_add=True)

  def save(self, *args, **kwargs):

    result = self.decrementar_cantidad()
    if result['total_cost'] > 0:
      self.total_costo = result['total_cost']
      super(Computadora, self).save(*args, **kwargs)
    else:
      raise ValidationError(result['no_Stock'])



  def decrementar_cantidad(self):
    value = {
      'no_Stock': '',
      'total_cost': 0
    }
    raton = Raton.objects.get(id = self.raton.id)
    teclado = Teclado.objects.get(id = self.teclado.id)
    monitor = Monitor.objects.get(id = self.monitor.id)
    altavoz = Altavoz.objects.get(id = self.altavoz.id)
    procesador = Procesador.objects.get(id = self.procesador.id)
    placabase = PlacaBase.objects.get(id = self.placabase.id)

    if (self.contadorComputadoras > raton.contadorRatones):
      value['no_Stock'] = raton.marca
      return value
    elif (self.contadorComputadoras > teclado.contadorTeclados):
      value['no_Stock'] = teclado.marca
      return value
    elif (self.contadorComputadoras > monitor.cantidad):
      value['no_Stock'] = monitor.marca
      return value
    elif (self.contadorComputadoras > altavoz.cantidad):
      value['no_Stock'] = altavoz.marca
      return value
    elif (self.contadorComputadoras > procesador.cantidad):
      value['no_Stock'] = procesador.marca + " " + procesador.descripcion
      return value
    elif(self.contadorComputadoras > placabase.cantidad):
      value['no_Stock'] = placabase.marca + " " + placabase.descripcion
      return value
    else:
      Monitor.objects.filter(id=self.monitor.id).update(cantidad = F('cantidad')-self.contadorComputadoras)
      Altavoz.objects.filter(id=self.altavoz.id).update(cantidad = F('cantidad')-self.contadorComputadoras)

      Raton.objects.filter(id=self.raton.id).update(contadorRatones = F('contadorRatones')-self.contadorComputadoras)
      Teclado.objects.filter(id=self.teclado.id).update(contadorTeclados = F('contadorTeclados')-self.contadorComputadoras)
    
      Procesador.objects.filter(id=self.procesador.id).update(cantidad = F('cantidad')-self.contadorComputadoras)
      PlacaBase.objects.filter(id=self.placabase.id).update(cantidad = F('cantidad')-self.contadorComputadoras)
      total = raton.costo + teclado.costo + monitor.costo + altavoz.costo + procesador.costo + placabase.costo
      value['total_cost'] = total
      return value

  def __str__(self) -> str:
    return f'{self.nombre} --- {self.contadorComputadoras} --- Q.{self.total_costo}'