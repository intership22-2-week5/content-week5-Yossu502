# django
from django.db import models
from django.db.models import F

# Create your models here.

class DispositivoDeEntrada(models.Model):
  """Crear objetos de tipo Dispositivo de entrada"""
  tipoDeEntrada = models.CharField(max_length=100)
  marca = models.CharField(max_length=100)

  def __str__(self) -> str:
    return f'{self.tipoDeEntrada} {self.marca}'

class Raton(DispositivoDeEntrada):
  """Crear Objetos de tipo Raton"""
  contadorRatones = models.IntegerField()

  def __str__(self) -> str:
    return f'{self.marca}'

class Teclado(DispositivoDeEntrada):
  """Crear objetos de tipo teclado"""
  contadorTeclados = models.IntegerField()

  def __str__(self) -> str:
    return f'{self.marca}'

class Monitor(models.Model):
  """Creat objetos de tipo Monitor"""
  marca = models.CharField(max_length=100)
  size = models.CharField(max_length=100)
  contadorMonitor = models.IntegerField()

  def __str__(self) -> str:
    return f'{self.marca} Tamaño: {self.size}'

class Computadora(models.Model):
  """Crear objetos de tipo computadora"""
  nombre = models.CharField(max_length=100)
  monitor = models.ForeignKey(Monitor, on_delete=models.CASCADE)
  teclado = models.ForeignKey(Teclado, on_delete=models.CASCADE)
  raton = models.ForeignKey(Raton, on_delete=models.CASCADE)
  contadorComputadoras = models.IntegerField()

  def __str__(self) -> str:
    return f'{self.nombre}'

  def save(self, *args, **kwargs):
    if ((Monitor.objects.get(id=self.monitor.id).contadorMonitor == 0)): 
      return self.monitor.marca
    elif (Teclado.objects.get(id=self.teclado.id).contadorTeclados == 0):
      return self.teclado.marca
    elif (Raton.objects.get(id=self.raton.id).contadorRatones == 0):
      return self.raton.marca
    else:
      Monitor.objects.filter(id=self.monitor.id).update(contadorMonitor=F('contadorMonitor') - 1)
      Teclado.objects.filter(id=self.teclado.id).update(contadorTeclados=F('contadorTeclados') - 1)
      Raton.objects.filter(id=self.raton.id).update(contadorRatones=F('contadorRatones') - 1)
      super(Computadora,self).save(*args, **kwargs)



  def __str__(self) -> str:
    return f'{self.nombre} {self.monitor} {self.teclado} {self.raton}'

class Orden(models.Model):
  """Crea objetos de tipo Orden y almacena un arreglo de objetos de tipo Computadora"""
  computadoras = models.ManyToManyField(Computadora)
  contadorOrdenes = models.IntegerField()

  def __str__(self) -> str:
    return f'{self.computadoras.nombre}'
	