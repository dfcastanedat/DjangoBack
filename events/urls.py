from rest_framework import routers
from .api import EventViewSet

router = routers.DefaultRouter()
router.register('api/Events', EventViewSet, 'Events')

urlpatterns = router.urls
