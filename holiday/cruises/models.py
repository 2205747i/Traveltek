from __future__ import unicode_literals

from django.template.defaultfilters import slugify
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
	slug = models.URLField(unique = True, blank = True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.code_to_cruise_id)
        super(Cruise, self).save(*args, **kwargs)

    def __str__(self):
        return "name: " + self.name + ", codetocruiseid: " + self.code_to_cruise_id


class CabinGrade(models.Model):
    description = models.CharField(null = False, default = None, max_length=128)
    price = models.CharField(null = False, default = None, max_length=128)
    grade_number = models.CharField(null = False, default = None, max_length=128)
    result_number = models.CharField(null = False, default = None, max_length=128)
    title = models.CharField(null = False, default = None, max_length=128)
    session_key = models.CharField(null = False, default = None, max_length=128)
    image = models.URLField(blank=True, null=False)
    cabin_code = models.CharField(null=False, default=None, max_length=128)
    farename = models.CharField(null=False, default=None, max_length=128)
    colour_code = models.CharField(null=False, default=None, max_length=128)
    position_forward = models.BooleanField(blank=True)
    position_rear = models.BooleanField(blank=True)
    position_middle = models.BooleanField(blank=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.code_to_cruise_id)
        super(CabinGrade, self).save(*args, **kwargs)

    def __str__(self):
        return "grade_number: " + self.grade_number + " title: " + self.title


class Cabin(models.Model):
    cabin_number = models.CharField(null=False, blank=True, max_length=128)
    deck_code = models.CharField(null=False, blank=True, max_length=128)
    deck_name = models.CharField(null=False, blank=True, max_length=128)
    x1 = models.IntegerField(null=False, blank=True)
    x2 = models.IntegerField(null=False, blank=True)
    y1 = models.IntegerField(null=False, blank=True)
    y2 = models.IntegerField(null=False, blank=True)
    image = models.URLField(null=False, blank=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.code_to_cruise_id)
        super(Cabin, self).save(*args, **kwargs)

    def __str__(self):
        return "cabin_number:  " + self.cabin_number + " deck_name: " + self.deck_name
    
