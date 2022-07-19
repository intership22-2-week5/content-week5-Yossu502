# django
from django.db import router
from django.urls import path

# rest framework
from rest_framework.routers import DefaultRouter

# views Sets
from .views import AutoresViewSet, ObraDeArteViewSet, ExposicionViewSet, PortafolioViewSet

router = DefaultRouter()
router.register(r'autores', AutoresViewSet)
router.register(r'obras', ObraDeArteViewSet)
router.register(r'exposicion', ExposicionViewSet)
router.register(r'portafolio', PortafolioViewSet)

urlpatterns = router.urls

urlpatterns += [

]