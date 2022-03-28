from api.models import Driver, Passenger, Bus, Journey, Seat, Trip
from api.serializers import DriverSerializer, PassengerSerializer, BusSerializer, JourneySerializer, SeatSerializer, TripSerializer
from rest_framework import viewsets
from django_property_filter import PropertyNumberFilter, PropertyFilterSet


class DriverViewSet(viewsets.ModelViewSet):
    queryset = Driver.objects.all()
    serializer_class = DriverSerializer
    filterset_fields = ['run']


class PassengerViewSet(viewsets.ModelViewSet):
    queryset = Passenger.objects.all()
    serializer_class = PassengerSerializer
    filterset_fields = ['run']


class BusViewSet(viewsets.ModelViewSet):
    queryset = Bus.objects.all()
    serializer_class = BusSerializer


class JourneyViewSet(viewsets.ModelViewSet):
    queryset = Journey.objects.all()
    serializer_class = JourneySerializer


class SeatViewSet(viewsets.ModelViewSet):
    queryset = Seat.objects.all()
    serializer_class = SeatSerializer
    filterset_fields = ['trip']


class TripFilterSet(PropertyFilterSet):
    capacity = PropertyNumberFilter(field_name='capacity', lookup_expr='gte')

    class Meta:
        model = Trip
        fields = ['capacity', 'journey']


class TripViewSet(viewsets.ModelViewSet):
    queryset = Trip.objects.all()
    serializer_class = TripSerializer
    filterset_class = TripFilterSet
