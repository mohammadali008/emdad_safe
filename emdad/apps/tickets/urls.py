app_name = "tickets"


from rest_framework.routers import DefaultRouter
from .views_api import TicketViewSet

router = DefaultRouter()
router.register('', TicketViewSet, basename='ticket')

urlpatterns = router.urls
