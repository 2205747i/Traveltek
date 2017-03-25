from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.core.urlresolvers import reverse

# Create your views here.
def home(request):
    if request.method == "GET":
        searchtext = request.GET.get('search_box', None)
        if searchtext == None:
            return render(request, 'sesh/search.html', {"none": ""})
        venues = Venue.objects.filter(name__contains=searchtext)
        return render(request, 'sesh/search.html', {"venues": venues})
    else:
        return render(request, 'sesh/search.html', {"nosearch": ""})
    return render(request, 'cruises/index.html')
