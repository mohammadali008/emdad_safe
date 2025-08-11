app_name = "services"


from rest_framework.routers import DefaultRouter
from .views_api import ServiceViewSet

router = DefaultRouter()
router.register('', ServiceViewSet, basename='service')

urlpatterns = router.urls
