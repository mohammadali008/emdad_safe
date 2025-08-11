app_name = "contact"


from rest_framework.routers import DefaultRouter
from .views_api import ContactRequestViewSet

router = DefaultRouter()
router.register('', ContactRequestViewSet, basename='contact')

urlpatterns = router.urls
