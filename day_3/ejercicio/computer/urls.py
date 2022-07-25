# django
from django.db import router
from django.urls import path, re_path

# rest framework
from rest_framework.routers import DefaultRouter

#view sets
from .viewsets.component import RatonViewSet, TecladoViewSet, MonitorViewSet, AltavozViewSet, PlacaBaseViewSet, ProcesadorViewSet, ComponenteMarcaView, ComponentesListView, ComponenteDayView
from .viewsets.computer import ComputadoraViewSet, ComputadoraDayViewSet
from .viewsets.order import OrdenViewSet


router = DefaultRouter()
router.register(r'raton', RatonViewSet)
router.register(r'teclado', TecladoViewSet)
router.register(r'monitor', MonitorViewSet)
router.register(r'altavoz', AltavozViewSet)
router.register(r'placabase', PlacaBaseViewSet)
router.register(r'procesador', ProcesadorViewSet)
router.register(r'computadora', ComputadoraViewSet)
router.register(r'orden', OrdenViewSet)
router.register(r'buscarmarca', ComponenteMarcaView)
router.register(r'componentedia', ComponenteDayView)
router.register(r'computadoradia', ComputadoraDayViewSet)


urlpatterns = router.urls

urlpatterns += [
  path('componentes/', ComponentesListView.as_view())

]