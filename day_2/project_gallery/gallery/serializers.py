# rest framework serializers
from rest_framework import serializers

#models

from .models import Autores, ObraDeArte, Exposicion, Portafolio

class AutoresSerializer(serializers.ModelSerializer):
  class Meta:
    model = Autores
    fields = '__all__'


class ObraDeArteSerializer(serializers.ModelSerializer):
  class Meta:
    model = ObraDeArte
    fields = '__all__'


class ExposicionSerializer(serializers.ModelSerializer):
  class Meta:
    model = Exposicion
    fields = '__all__'


class PortafolioSerializer(serializers.ModelSerializer):
  class Meta:
    model = Portafolio
    fields = '__all__'