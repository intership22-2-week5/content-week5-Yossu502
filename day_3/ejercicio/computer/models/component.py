# django
from django.db import models

"""Clases que arman una computadora"""

class Componente(models.Model):
  component = (
    ('Teclado', 'Teclado'), 
    ('Raton', 'Raton'), 
    ('Monitor', 'Monitor'), 
    ('Altavoces', 'Altavoces'), 
    ('Placabase', 'Placabase'), 
    ('Procesador', 'Procesador')
  )
  type_component = models.CharField(choices=component, max_length=100)

  def __str__(self) -> str:
    return f'{self.type_component}'


class DispositivoDeSalida(Componente):
  marca = models.CharField(max_length=100)
  costo = models.IntegerField()

  def __str__(self) -> str:
    return f'{self.marca} {self.costo}'

class Monitor(DispositivoDeSalida):
  """Creat objetos de tipo Monitor"""
  descripcion = models.CharField(max_length=100)
  cantidad = models.IntegerField()
  fechaIngreso = models.DateTimeField(auto_now_add=True)

  def __str__(self) -> str:
    return f'{self.marca} -- {self.cantidad} -- Q.{self.costo}'

class Altavoz(DispositivoDeSalida):
  """Creat objetos de tipo Altaxo"""
  descripcion = models.CharField(max_length=100)
  cantidad = models.IntegerField()
  fechaIngreso = models.DateTimeField(auto_now_add=True)

  def __str__(self) -> str:
    return f'{self.marca} -- {self.cantidad} -- Q.{self.costo}'


class DispositivoInterno(Componente):
  marca = models.CharField(max_length=100)
  costo = models.IntegerField()

  def __str__(self) -> str:
    return f'{self.marca} {self.costo}'

class Procesador(DispositivoInterno):
  descripcion = models.CharField(max_length=100)
  cantidad = models.IntegerField()
  fechaIngreso = models.DateTimeField(auto_now_add=True)

  def __str__(self) -> str:
    return f'{self.marca} {self.descripcion} -- {self.cantidad} -- Q.{self.costo}'

class PlacaBase(DispositivoInterno):
  descripcion = models.CharField(max_length=100)
  cantidad = models.IntegerField()
  fechaIngreso = models.DateTimeField(auto_now_add=True)

  def __str__(self) -> str:
    return f'{self.marca} {self.descripcion} -- {self.cantidad} -- Q.{self.costo}'


class DispositivoDeEntrada(Componente):
  """Crear objetos de tipo Dispositivo de entrada"""
  marca = models.CharField(max_length=100)
  costo = models.IntegerField()

  def __str__(self) -> str:
    return f'{self.marca} {self.costo}'

class Raton(DispositivoDeEntrada):
  """Crear Objetos de tipo Raton"""
  contadorRatones = models.IntegerField()
  fechaIngreso = models.DateTimeField(auto_now_add=True)

  def __str__(self) -> str:
    return f'{self.marca} -- {self.contadorRatones} -- Q.{self.costo}'

class Teclado(DispositivoDeEntrada):
  """Crear objetos de tipo teclado"""
  contadorTeclados = models.IntegerField()
  fechaIngreso = models.DateTimeField(auto_now_add=True)

  def __str__(self) -> str:
    return f'{self.marca} -- {self.contadorTeclados} -- Q.{self.costo}'
