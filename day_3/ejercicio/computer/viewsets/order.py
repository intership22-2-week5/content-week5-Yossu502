# django rest framework
from rest_framework import viewsets

# modelos
from ..models.order import Orden

# serializadores
from ..serializers.order import OrdenSerializer


class OrdenViewSet(viewsets.ModelViewSet):
  queryset = Orden.objects.all()
  serializer_class = OrdenSerializer