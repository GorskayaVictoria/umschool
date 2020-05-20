
from rest_framework.routers import DefaultRouter

from api.views import PostViewSet, TaskViewSet

router = DefaultRouter()
router.register(r'pos1ts', PostViewSet, basename='api-post')
router.register(r'tas1ks', TaskViewSet, basename='api-channel')
urlpatterns = router.urls