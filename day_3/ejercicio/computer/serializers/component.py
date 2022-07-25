# django rest framework
from rest_framework import serializers

# modelos componentes
from ..models.component import Componente, DispositivoDeEntrada, DispositivoDeSalida, DispositivoInterno, Raton, Teclado, Monitor, Altavoz, PlacaBase, Procesador


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

class AltavozSerializer(serializers.ModelSerializer):
  class Meta:
    model = Altavoz
    fields = '__all__'


class PlacaBaseSerializer(serializers.ModelSerializer):
  class Meta:
    model = PlacaBase
    fields = '__all__'


class ProcesadorSerializer(serializers.ModelSerializer):
  class Meta:
    model = Procesador
    fields = '__all__'


class ComponenteSerializer(serializers.ModelSerializer):
  class Meta:
    model = Componente
    fields = '__all__'

  def to_representation(self, instance):
    if instance.type_component == 'Raton':
      return {
        'id': instance.id,
        'type_component': instance.type_component,
        'marca': Raton.objects.get(id=instance.id).marca
      }
    elif instance.type_component == 'Teclado':
      return {
        'id': instance.id,
        'type_component': instance.type_component,
        'marca': Teclado.objects.get(id=instance.id).marca
      }
    elif instance.type_component == 'Monitor':
      return {
        'id': instance.id,
        'type_component': instance.type_component,
        'descripcion': Monitor.objects.get(id=instance.id).marca + " " + Monitor.objects.get(id=instance.id).descripcion
      }
    elif instance.type_component == 'Altavoces':
      return {
        'id': instance.id,
        'type_component': instance.type_component,
        'descripcion': Altavoz.objects.get(id=instance.id).marca + " " + Altavoz.objects.get(id=instance.id).descripcion
      }
    elif instance.type_component == 'Procesador':
      return {
        'id': instance.id,
        'type_component': instance.type_component,
        'descripcion': Procesador.objects.get(id=instance.id).marca + " " + Procesador.objects.get(id=instance.id).descripcion
      }
    elif instance.type_component == 'Placabase':
      return {
        'id': instance.id,
        'type_component': instance.type_component,
        'descripcion': PlacaBase.objects.get(id=instance.id).marca + " " + PlacaBase.objects.get(id=instance.id).descripcion
      }

class ComponenteMarcaSerializer(serializers.ModelSerializer):
  class Meta:
    model = Componente
    fields = '__all__'
