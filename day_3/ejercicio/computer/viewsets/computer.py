# django rest framework
from rest_framework import viewsets, views, status
from django.forms import ValidationError
from django.utils import timezone

# model
from ..models.computer import Computadora

# serializadores
from ..serializers.computer import ComputadoraSerializer, ComputadoraDiaSerializer


class ComputadoraViewSet(viewsets.ModelViewSet):
  queryset = Computadora.objects.all()
  serializer_class = ComputadoraSerializer

  def create(self, request, *args, **kwargs):
    try:
      super().create(request, *args, **kwargs)
      return views.Response({'message': 'Computadora Creada',
      }, status=status.HTTP_201_CREATED)
    except ValidationError as res:
      return views.Response({'message': 'Computadora no guardada',
      'Componente sin stock': res.message, 
      "stock": False}, status=status.HTTP_400_BAD_REQUEST)

class ComputadoraDayViewSet(viewsets.ModelViewSet):
  queryset = Computadora.objects.all()
  serializer_class = ComputadoraDiaSerializer

  def obtenerDatosComputadora(self, yesterday, today):
      computadoraC = Computadora.objects.filter(fecha__range=(yesterday, today))
      if computadoraC:
        serializer = ComputadoraDiaSerializer(computadoraC, many=True)
        return views.Response({'status': True, 'message': 'Componentes encontrados',
        'data': serializer.data}, status=status.HTTP_200_OK)
      else:
        return views.Response({'status': False, 'message': 'No hay componentes creados hace un dia',}
        , status=status.HTTP_204_NO_CONTENT)

  def list(self, request, *args, **kwargs):
      try:
        yesterday = timezone.now() - timezone.timedelta(days=1)
        today = timezone.now() #- timezone.timedelta(days=3)
        tipo = request.query_params.get('tipo')
        if tipo == 'computadora':
          return self.obtenerDatosComputadora(yesterday, today)
        else:
          return views.Response({'message': 'No envio ninguna query valida',
          'status': False}, status=status.HTTP_404_NOT_FOUND)
      except Exception as e:
        return views.Response({'message': 'Error',
        'status': str(e)}, status=status.HTTP_400_BAD_REQUEST)