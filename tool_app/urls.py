from rest_framework import routers
from .api import ToolViewSet


router = routers.DefaultRouter()
router.register('api/tool', ToolViewSet, 'tool')


urlpatterns = router.urls