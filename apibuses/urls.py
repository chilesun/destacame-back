from django.urls import include, path
from api import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'bus', views.BusViewSet)
router.register(r'driver', views.DriverViewSet)
router.register(r'journey', views.JourneyViewSet)
router.register(r'passenger', views.PassengerViewSet)
router.register(r'seat', views.SeatViewSet)
router.register(r'trip', views.TripViewSet)


urlpatterns = [
    path('api/', include(router.urls)),
]
