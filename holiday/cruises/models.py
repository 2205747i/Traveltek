from __future__ import unicode_literals

from django.db import models

class Cruise(models.Model):
	code_to_cruise_id = models.CharField(unique = True, null = False, default = None)
	sail_date = models.DateTimeField(null = False, default = None)
	sail_nights = models.IntegerField(null = false, default = 0)
	cruise_id = models.CharField(null = False, default = None)
	line_id = models.CharField(null = False, default = None)
	region_id = models.CharField(null = False, default = None)
	