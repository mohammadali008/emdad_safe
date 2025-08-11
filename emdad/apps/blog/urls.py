app_name = "blog"


from rest_framework.routers import DefaultRouter
from .views_api import BlogPostViewSet

router = DefaultRouter()
router.register('', BlogPostViewSet, basename='blog')

urlpatterns = router.urls
