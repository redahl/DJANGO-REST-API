from rest_framework import routers
from .api import ProjectViewSet

router = routers.DefaultRouter()

router.register('api/projectocrud', ProjectViewSet, 'projects')

urlpatterns = router.urls
