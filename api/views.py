from django.shortcuts import render
from django.db.models import Count

from api.models import Driver, Passenger, Bus, Journey, Seat, Trip
from api.serializers import DriverSerializer, PassengerSerializer, BusSerializer, JourneySerializer, SeatSerializer, TripSerializer
from rest_framework import viewsets
import django_filters.rest_framework


class DriverViewSet(viewsets.ModelViewSet):
    queryset = Driver.objects.all()
    serializer_class = DriverSerializer
    filter_backends = [django_filters.rest_framework.DjangoFilterBackend]
    filterset_fields = ['run']


class PassengerViewSet(viewsets.ModelViewSet):
    queryset = Passenger.objects.all()
    serializer_class = PassengerSerializer
    filter_backends = [django_filters.rest_framework.DjangoFilterBackend]
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
    filter_backends = [django_filters.rest_framework.DjangoFilterBackend]
    filterset_fields = ['trip']

class TripViewSet(viewsets.ModelViewSet):
    queryset = Trip.objects.all()
    serializer_class = TripSerializer

    def get_queryset(self):
        gt = self.request.GET.get('capacity__gt')
        if gt:
            comply = list()
            seats = Seat.objects.exclude(passenger=None).values('trip').order_by('trip').annotate(count=Count('trip'))
            for seat in seats:
                if seat['count'] * 10 >= float(gt):
                    comply.append(seat['trip'])
            return self.queryset.filter(id__in=comply)
        return self.queryset


