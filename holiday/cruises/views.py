from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.core.urlresolvers import reverse

# Create your views here.
def home(request):

    return render(request, 'cruises/index.html')

def test(request):
	print(request.data)
	cruises = Cruise.objects.filter()
	context_dict["cruises"] = cruises
	return render(request, results.html, context_dict);