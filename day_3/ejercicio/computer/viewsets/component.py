# django rest framework
from django.forms import ValidationError
from rest_framework import viewsets, views, generics, status
from django.utils  import timezone

# otthers 
from itertools import chain

from computer.models.computer import Computadora 

# modelos
from ..models.component import Raton, Teclado, Monitor, Altavoz, Procesador, PlacaBase, Componente, DispositivoDeEntrada, DispositivoDeSalida, DispositivoInterno

# serializadores
from ..serializers.component import RatonSerializer, TecladoSerializer, MonitorSerializer, AltavozSerializer, PlacaBaseSerializer, ProcesadorSerializer, ComponenteMarcaSerializer, ComponenteSerializer

class RatonViewSet(viewsets.ModelViewSet):
  queryset = Raton.objects.all()
  serializer_class = RatonSerializer


class TecladoViewSet(viewsets.ModelViewSet):
  queryset = Teclado.objects.all()
  serializer_class = TecladoSerializer


class MonitorViewSet(viewsets.ModelViewSet):
  queryset = Monitor.objects.all()
  serializer_class = MonitorSerializer


class AltavozViewSet(viewsets.ModelViewSet):
  queryset = Altavoz.objects.all()
  serializer_class = AltavozSerializer


class ProcesadorViewSet(viewsets.ModelViewSet):
  queryset = Procesador.objects.all()
  serializer_class = ProcesadorSerializer


class PlacaBaseViewSet(viewsets.ModelViewSet):
  queryset = PlacaBase.objects.all()
  serializer_class = PlacaBaseSerializer


class ComponentesListView(generics.ListAPIView):
  serializer_class = ComponenteSerializer

  def onlyByTipo(self, type_content):
    disp_entrada = DispositivoDeEntrada.objects.all()
    disp_salida = DispositivoDeSalida.objects.all()
    disp_interno = DispositivoInterno.objects.all()
    if type_content == 'dispositivodeentrada':
      return disp_entrada
    elif type_content == 'dispositivodesalida':
      return disp_salida
    elif type_content == 'dispositivointerno':
      return disp_interno
    else:
      return None

  def onlyByTipoAndCantidad(self, type_content, cantidad):
    ratonC = Raton.objects.filter(contadorRatones=cantidad)
    tecladoC = Teclado.objects.filter(contadorTeclados=cantidad)
    monitorC =  Monitor.objects.filter(cantidad=cantidad)
    altavozC =  Altavoz.objects.filter(cantidad=cantidad)
    procesadorC =  Procesador.objects.filter(cantidad=cantidad)
    placaC =  PlacaBase.objects.filter(cantidad=cantidad)

    if type_content == 'dispositivodeentrada':
      return chain(ratonC, tecladoC)
    elif type_content == 'dispositivodesalida':
      return chain(monitorC, altavozC)
    elif type_content == 'dispositivointerno':
      return chain(procesadorC, placaC)
    else:
      return None



  def get_queryset(self):
    type_component = self.request.query_params.get('tipo')
    cantidad = self.request.query_params.get('cantidad')
    if cantidad == None:
      return self.onlyByTipo(type_component)
    elif cantidad != None:
      return self.onlyByTipoAndCantidad(type_component, cantidad)
    else:
      return None


class ComponenteMarcaView(viewsets.ModelViewSet):
  queryset = Componente.objects.all()
  serializer_class = ComponenteMarcaSerializer

  def getByMarca(self, busqueda):
    marca_entrada = DispositivoDeEntrada.objects.filter(marca__contains=busqueda)
    marca_salida = DispositivoDeSalida.objects.filter(marca__contains=busqueda)
    marca_interna = DispositivoInterno.objects.filter(marca__contains=busqueda)

    if marca_entrada or marca_salida or marca_interna:
      marcafinal = chain(marca_interna, marca_entrada, marca_salida)
      serializer = ComponenteMarcaSerializer(marcafinal, many=True)
      return views.Response({'status': True, 'message': 'Componentes encontrados',
      'data': serializer.data}, status=status.HTTP_200_OK)
    else:
      return views.Response({'message': 'No hay componenetes de esa marca',
      'status': False}, status=status.HTTP_204_NO_CONTENT)

  def list(self, request, *args, **kwargs):
    try:
      marca_buscada = request.query_params.get('marca')
      if marca_buscada:
        return self.getByMarca(marca_buscada)
      else:
        return views.Response({'message': 'No envio ninguna query valida',
      'status': False}, status=status.HTTP_404_NOT_FOUND)
    except Exception as e:
      return views.Response({'message': 'Error',
      'status': str(e)}, status=status.HTTP_400_BAD_REQUEST)


class ComponenteDayView(viewsets.ModelViewSet):
    queryset = Componente.objects.all()
    serializer_class = ComponenteMarcaSerializer
    
    def obtenerDatosComponentes(self, yesterday, today):
      ratonC = Raton.objects.filter(fechaIngreso__range=(yesterday, today))
      tecladoC = Teclado.objects.filter(fechaIngreso__range=(yesterday, today))
      monitorC =  Monitor.objects.filter(fechaIngreso__range=(yesterday, today))
      altavozC =  Altavoz.objects.filter(fechaIngreso__range=(yesterday, today))
      procesadorC = Procesador.objects.filter(fechaIngreso__range=(yesterday, today)) 
      placaC =  PlacaBase.objects.filter(fechaIngreso__range=(yesterday, today))
      if ratonC or tecladoC or monitorC or altavozC or procesadorC or placaC:
        finalData = chain(ratonC, tecladoC, monitorC, altavozC, procesadorC, placaC)
        serializer = ComponenteMarcaSerializer(finalData, many=True)
        return views.Response({'status': True, 'message': 'Componentes encontrados',
        'data': serializer.data}, status=status.HTTP_200_OK)
      else:
        return views.Response({'status': False, 'message': 'No hay componentes creados hace un dia',}
        , status=status.HTTP_204_NO_CONTENT)


    def list(self, request, *args, **kwargs):
      try:
        yesterday = timezone.now() - timezone.timedelta(days=1)
        today = timezone.now() #  - datetime.timedelta(days=2)
        tipo = request.query_params.get('tipo')
        if tipo == 'componente':
          return self.obtenerDatosComponentes(yesterday, today)
        else:
          return views.Response({'message': 'No envio ninguna query valida',
          'status': False}, status=status.HTTP_404_NOT_FOUND)
      except Exception as e:
        return views.Response({'message': 'Error',
        'status': str(e)}, status=status.HTTP_400_BAD_REQUEST)