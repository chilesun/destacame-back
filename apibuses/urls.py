"""apibuses URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
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
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
]
