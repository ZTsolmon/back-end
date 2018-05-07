from rest_framework.routers import DefaultRouter
from .views import ShipViewSet, UserViewSet

router = DefaultRouter()
router.register('ships', ShipViewSet, base_name='ships')
router.register('users', UserViewSet)