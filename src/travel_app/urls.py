from rest_framework import routers, urlpatterns
from . import views

router = routers.SimpleRouter()
router.register('', views.TravelAppViewSet, basename="TravelApp")
urlpatterns = router.urls