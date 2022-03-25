from itertools import cycle
from django.db import models
from django.core.validators import MaxValueValidator
import datetime


class Person(models.Model):
	name = models.CharField(max_length=40)
	last_name = models.CharField(max_length=40)
	run = models.IntegerField(unique=True, validators=[MaxValueValidator(99999999)])

	@property
	def check_digit(self):
		reverse_run = map(int, reversed(str(self.run)))
		factors = cycle(range(2, 8))
		r = sum(d * f for d, f in zip(reverse_run, factors))
		if (-r) % 11 == 10:
			return 'K'
		else: 
			return (-r) % 11

	class Meta:
		abstract = True


class Passenger(Person):
	pass


class Driver(Person):
	pass


class Bus(models.Model):
	number_plate = models.CharField(max_length=6)
	seats = models.IntegerField(default=10, editable=False)
	driver = models.ForeignKey(Driver, on_delete=models.SET_NULL, null=True)


class Journey(models.Model):
	origin = models.CharField(max_length=40)
	destination = models.CharField(max_length=40)
	duration = models.FloatField()


class Trip(models.Model):
	bus = models.ForeignKey(Bus, on_delete=models.SET_NULL, null=True)
	journey = models.ForeignKey(Journey, on_delete=models.CASCADE)
	start_time = models.DateTimeField()

	@property
	def end_time(self):
		date1 = self.start_time
		plus = self.journey.duration
		date2 = date1 + datetime.timedelta(hours=plus)
		return date2

	def save(self, *args, **kwargs):
		super(Trip, self).save(*args, **kwargs)
		if not len(Seat.objects.filter(trip=self)):
			for i in range(self.bus.seats):
				Seat(number=i + 1, trip=self).save()


class Seat(models.Model):
	passenger = models.ForeignKey(Passenger, on_delete=models.SET_NULL, null=True, blank=True)
	trip = models.ForeignKey(Trip, on_delete=models.CASCADE)
	number = models.PositiveIntegerField()

