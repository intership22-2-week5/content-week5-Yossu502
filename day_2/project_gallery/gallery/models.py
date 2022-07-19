from django.db import models

# Create your models here.

class Autores(models.Model):
  nombre = models.CharField(max_length=100)
  apellido = models.CharField(max_length=100)
  pais = models.CharField(max_length=100)
  edad = models.CharField(max_length=10)

  def __str__(self) -> str:
    return f'{self.nombre}  {self.apellido}'

class ObraDeArte(models.Model):
  nombreObra = models.CharField(max_length=100)
  tipoDeObra = models.CharField(max_length=100)
  autores = models.ManyToManyField(Autores)
  fechaCreacion = models.CharField(max_length=10)
  valorEstimado = models.IntegerField()
  fotosVideos = models.CharField(max_length=100)

  def __str__(self) -> str:
    return f'{self.nombreObra} {self.autores}'



class Portafolio(models.Model):
  nombrePortafolio = models.CharField(max_length=100)
  obrasDeArte = models.ManyToManyField(ObraDeArte)

  def __str__(self) -> str:
    return f'{self.nombrePortafolio} {self.obrasDeArte}'


class Exposicion(models.Model):
  nombreExpo = models.CharField(max_length=100)
  fechaExpo = models.CharField(max_length=100)
  lugarExpo = models.CharField(max_length=100)
  descripcionExpo = models.CharField(max_length=100)
  portafolioExpo = models.ForeignKey(Portafolio, on_delete=models.CASCADE)

  def __str__(self) -> str:
    return f'{self.nombreExpo} {self.fechaExpo} {self.lugarExpo} {self.obrasDeArte}'

