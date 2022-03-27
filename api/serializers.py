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
	end_time = serializers.ReadOnlyField
	capacity = serializers.ReadOnlyField

	class Meta:
		model = Trip
		fields = ['id', 'bus', 'journey', 'start_time', 'end_time', 'capacity']


class SeatSerializer(serializers.ModelSerializer):
    class Meta:
        model = Seat
        fields = '__all__'