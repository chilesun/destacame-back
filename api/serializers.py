from api.models import Seat, Bus, Driver, Passenger, Journey, Trip
from rest_framework import serializers


class DriverSerializer(serializers.ModelSerializer):
	check_digit = serializers.ReadOnlyField

	class Meta:
		model = Driver
		fields = ['id' ,'name', 'last_name','run', 'check_digit']


class PassengerSerializer(serializers.ModelSerializer):
	check_digit = serializers.ReadOnlyField

	class Meta:
		model = Passenger
		fields = ['id' ,'name', 'last_name','run', 'check_digit']


class JourneySerializer(serializers.ModelSerializer):

	class Meta:
		model = Journey
		fields = '__all__'


class BusSerializer(serializers.ModelSerializer):
	class Meta:
		model = Bus
		fields = '__all__'


class TripSerializer(serializers.ModelSerializer):
	capacity = serializers.SerializerMethodField()
	end_time = serializers.ReadOnlyField

	class Meta:
		model = Trip
		fields = ['id', 'bus', 'driver', 'journey', 'start_time', 'end_time', 'capacity']
		read_only_fields = ['capacity']

	def get_capacity(self, obj):
		seats = Seat.objects.filter(trip=obj)
		return f'{(len(seats.exclude(passenger=None)) / len(seats)) * 100}'


class SeatSerializer(serializers.ModelSerializer):
    class Meta:
        model = Seat
        fields = '__all__'