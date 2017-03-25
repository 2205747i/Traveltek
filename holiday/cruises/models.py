from __future__ import unicode_literals

from django.db import models

class Cruise(models.Model):
	# air_balcony = models.IntegerField(default=0)
	# airbalcony_pricecode = models.IntegerField(null = True)
	# airinside = models.IntegerField(default=0)
	# airinside_pricecode = models.IntegerField(null = True)
	# airport = models.CharField(null = True)
	# airport_name = models.CharField(null = True)
	# airsuite = models.IntegerField(default=0)
	# airsuite_pricecode = models.IntegerField(null = True)
	# altvoyagecode = models.IntegerField(default = None)

	# copyandmedia = models.CharField(default = "")
	# line_id = models.CharField(null = False, default = None)
	# region_id = models.CharField(null=False, default=None)

	sail_date = models.DateTimeField(null = False, default = None)
	nights = models.IntegerField(null = False, default = None)
	sail_nights = models.IntegerField(null = False, default = 0)
	# cruise_id = models.CharField(null = False, default = None, max_length=128)
	name = models.CharField(null = False, default = None, max_length=128)
	code_to_cruise_id = models.CharField(unique=True, null=False, max_length=128, primary_key=True)

	def __str__(self):
		return "name: " + self.name + " codetocruiseid: " + self.code_to_cruise_id

# class Hotel(models.Model):
# 	name = models.CharField(null = False, default = None, max_length=128)
# 	image = models.URLField(null = False, default = None)
# 	description = models.CharField(null = False, default = None, max_length=128)
# 	checkin = models.DateField(null = False, default = None)
# 	lat = models.CharField(null = False, default = None, max_length=128)
# 	lon = models.CharField(null = False, default = None, max_length=128)
# 	cheapestprice = models.FloatField(null = False, default = None)
#
# 	def __str__(self):
# 		return "name: " + self.name
#
# class Flight(models.Model):
# 	carrier = models.CharField(null = False, default = None, max_length=128)
#
