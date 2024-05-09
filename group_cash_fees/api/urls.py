from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .collects.views import CollectViewSet
from .organizations.views import OrganizationViewSet
from .payments.views import PaymentsViewSet
from .users.views import CustomUserViewSet

app_name = 'api'
VERSION = 'v1'


router_1 = DefaultRouter()


router_1.register('organizations',
                  OrganizationViewSet, basename='organizations')
router_1.register('collects',
                  CollectViewSet, basename='collects')
router_1.register(r'collects/(?P<collect_id>\d+)/payments',
                  PaymentsViewSet, basename='payments')
router_1.register('users', CustomUserViewSet, basename='users')


urlpatterns = [
    path(f'{VERSION}/', include((router_1.urls))),
    path(f'{VERSION}/auth/', include('djoser.urls.authtoken')),
]
