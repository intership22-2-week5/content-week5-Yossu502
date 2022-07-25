# django rest framework
from rest_framework import serializers

# modelo 
from ..models.order import Orden
from ..models.computer import Computadora


class OrdenSerializer(serializers.ModelSerializer):
  computadoras = serializers.SlugRelatedField(queryset=Computadora.objects.all(), many=True, slug_field='nombre')
  class Meta:
    model = Orden
    exclude = ('fecha',)
    read_only_fields = ['total_costo']
