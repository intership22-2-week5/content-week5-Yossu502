# django rest framework
from rest_framework import serializers

# modelos
from ..models.computer import Computadora


class ComputadoraSerializer(serializers.ModelSerializer):
  class Meta:
    model = Computadora
    exclude = ('fecha',)
    read_only_fields = ['total_costo']
  def to_representation(self, instance):
    return {
      'id': instance.id,
      'nombre': instance.nombre,
      'contadorComputadoras': instance.contadorComputadoras,
      'total_costo': instance.total_costo,
      'procesador': instance.procesador.marca + " " + instance.procesador.descripcion,
      'placabase': instance.placabase.marca + " " + instance.placabase.descripcion,
      'monitor': instance.monitor.marca + " " + instance.monitor.descripcion,
      'altavoz': instance.altavoz.marca + " " + instance.altavoz.descripcion,
      'teclado': instance.teclado.marca,
      'raton': instance.raton.marca
    }

class ComputadoraDiaSerializer(serializers.ModelSerializer):
  class Meta:
    model = Computadora
    fields = '__all__'
  def to_representation(self, instance):
    return {
      'id': instance.id,
      'nombre': instance.nombre,
      'contadorComputadoras': instance.contadorComputadoras,
      'total_costo': instance.total_costo,
      'procesador': instance.procesador.marca + " " + instance.procesador.descripcion,
      'placabase': instance.placabase.marca + " " + instance.placabase.descripcion,
      'monitor': instance.monitor.marca + " " + instance.monitor.descripcion,
      'altavoz': instance.altavoz.marca + " " + instance.altavoz.descripcion,
      'teclado': instance.teclado.marca,
      'raton': instance.raton.marca
    }