#Django Rest Framework
from rest_framework.views import Response
from rest_framework import viewsets

# models
from .models import Autores, ObraDeArte, Exposicion, Portafolio

# serializers

from .serializers import AutoresSerializer, ObraDeArteSerializer, ExposicionSerializer, PortafolioSerializer

class AutoresViewSet(viewsets.ModelViewSet):
  queryset = Autores.objects.all()
  serializer_class = AutoresSerializer


class ObraDeArteViewSet(viewsets.ModelViewSet):
  queryset = ObraDeArte.objects.all()
  serializer_class = ObraDeArteSerializer


class ExposicionViewSet(viewsets.ModelViewSet):
  queryset = Exposicion.objects.all()
  serializer_class = ExposicionSerializer

class PortafolioViewSet(viewsets.ModelViewSet):
  queryset = Portafolio.objects.all()
  serializer_class = PortafolioSerializer