
app_name = 'accounts'
#
from django.urls import path
from .views_api import SendCodeView, VerifyCodeView
from .views_api import UserViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'users', UserViewSet, basename='users')

urlpatterns = [
    path('send-code/', SendCodeView.as_view(), name='send-code'),
    path('verify-code/', VerifyCodeView.as_view(), name='verify-code'),
]

urlpatterns += router.urls
