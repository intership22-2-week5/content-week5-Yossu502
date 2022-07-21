# rest framework
from rest_framework import serializers

# models

from .models import Raton, Teclado, Monitor, Computadora, Orden

class RatonSerializer(serializers.ModelSerializer):
  class Meta:
    model = Raton
    fields = '__all__'


class TecladoSerializer(serializers.ModelSerializer):
  class Meta:
    model = Teclado
    fields = '__all__'


class MonitorSerializer(serializers.ModelSerializer):
  class Meta:
    model = Monitor
    fields = '__all__'


class ComputadoraSerializer(serializers.ModelSerializer):
  class Meta:
    model = Computadora
    fields = '__all__'

  def to_representation(self, instance):
    return {
      'id': instance.id,
      'nombre': instance.nombre,
      'monitor': instance.monitor.marca + " " + instance.monitor.size,
      'teclado': instance.teclado.tipoDeEntrada + " " + instance.teclado.marca,
      'raton': instance.raton.tipoDeEntrada + " " + instance.raton.marca,
    }

class OrdenSerializer(serializers.ModelSerializer):
  computadoras = serializers.SlugRelatedField(queryset=Computadora.objects.all(), many=True, slug_field='nombre')
  class Meta:
    model = Orden
    fields = ['id', 'contadorOrdenes', 'computadoras']

  # def to_representation(self, instance):
  #   return {
  #     'id': instance.id,
  #     'computadoras': instance.computadoras.nombre
  #   }