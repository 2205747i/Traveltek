from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.template.defaultfilters import slugify
from datetime import datetime
from cruises.models import Cruise

# Create your views here.
def home(request):
    return render(request, 'cruises/index.html')

def form(request):
	return render(request, 'cruises/form.html')

def test(request):
	print "got it"
	context_dict = {}
	if request.method == "POST":
		start_date = request.POST["start"]
		start_date = datetime.strptime(start_date, '%Y-%m-%d')
		end_date = request.POST["end"]
		end_date = datetime.strptime(end_date, '%Y-%m-%d')
		cruises = Cruise.objects.filter(sail_date__range = [start_date, end_date])
		context_dict["cruises"] = cruises
	# cruises = Cruise.objects.filter()
	# context_dict["cruises"] = cruises
	return render(request, 'cruises/results.html', context_dict);