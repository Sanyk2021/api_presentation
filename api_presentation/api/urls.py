from rest_framework.routers import DefaultRouter

from django.urls import path, include

from .views import AlbumViewSet

router = DefaultRouter()

app_name = 'api'

router.register('album', AlbumViewSet)

urlpatterns = [
    path('v1/', include(router.urls)),
]
