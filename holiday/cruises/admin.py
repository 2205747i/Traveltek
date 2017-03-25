from django.contrib import admin
from cruises.models import Cruise, CabinGrade, Cabin

# Register your models here.

admin.site.register(Cruise)
admin.site.register(CabinGrade)
admin.site.register(Cabin)