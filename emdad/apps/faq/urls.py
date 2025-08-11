app_name = "faq"


from rest_framework.routers import DefaultRouter
from .views_api import FAQViewSet

router = DefaultRouter()
router.register('', FAQViewSet, basename='faq')

urlpatterns = router.urls
