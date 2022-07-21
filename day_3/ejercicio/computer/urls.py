# django
from django.db import router
from django.urls import path

# rest framework
from rest_framework.routers import DefaultRouter

#view sets

from .views import RatonViewSet, TecladoViewSet, MonitorViewSet, ComputadoraViewSet, OrdenViewSet

router = DefaultRouter()
router.register(r'raton', RatonViewSet)
router.register(r'teclado', TecladoViewSet)
router.register(r'monitor', MonitorViewSet)
router.register(r'computadora', ComputadoraViewSet)
router.register(r'orden', OrdenViewSet)

urlpatterns = router.urls

urlpatterns += [

]