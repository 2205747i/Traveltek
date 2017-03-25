from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.core.urlresolvers import reverse
import requests
from lxml import etree
from datetime import datetime
from cruises.models import Cruise, CabinGrade

# Create your views here.
def home(request):
    return render(request, 'cruises/home.html')

def form(request):
    return render(request, 'cruises/form.html')

def show_cruise(request, code):
    context_dict = {}
    try:
        cruise = Cruise.objects.get(code_to_cruise_id = code)
        testreq = '''<?xml version="1.0"?>
<request>
 <auth username="hackathon" password="pr38ns48" />
 <method action="simplesearch" sitename="cruisedemo.traveltek.net"
 status="Live" type="cruise">
 <searchdetail 
					type="cruise" adults="2" children="0" codetocruiseid="955202" sid="30115" resultkey="default">
					</searchdetail>
 </method>
</request>'''.format(cruise.adults, cruise.children)
		
        r = requests.post('https://fusionapi.traveltek.net/0.9/interface.pl', data = {"xml": testreq})
		
        root = etree.fromstring(r.text)
		
        for element in root.iterfind("request/method"):
            seshkey = element.get('sessionkey')

        testreq = '''<?xml version="1.0"?>
		<request>
			<auth username="hackathon" password="pr38ns48" />
			<method action="getcabingrades" sitename="cruisedemo.traveltek.net" sessionkey="{0}" resultno="302_0.0"/>
		</request>'''.format(seshkey,)
		
        r = requests.post('https://fusionapi.traveltek.net/0.9/interface.pl', data = {"xml": testreq})
        root = etree.fromstring(r.text)
        print(r.text)
        resultno = root.find("request/method")
        resultno = resultno.get('resultno')
        print resultno
        context_dict = {}
        context_dict["cabingrades"] = []
        for element in root.iterfind("results/grades/grade"):
        	title = element.get('description')
        	cabincode = element.get('cabincode')
        	farename = element.get('farename')
        	colourcode = element.get('colourcode')
        	gradeno = element.get('gradeno')
        	price = element.get('price')
        	print(title)
      		print(price)
        	# description = cabintype.get('description')
        	# image = cabintype.get('imageurl')
        	# cabintype = cabintype.find("position")
        	# forward = cabintype.get('forward')
        	# middle = cabintype.get('middle')
        	# rear = cabintype.get('rear')
        	cg = CabinGrade.objects.get_or_create(title = title, price = price, grade_number = gradeno, result_number = resultno, session_key = seshkey,
        		cabin_code = cabincode, farename = farename)[0]
        	context_dict["cabingrades"] = context_dict["cabingrades"] +[cg]

        	cg.save()
        return render(request, 'cruises/cruise.html', context_dict)



    except Cruise.DoesNotExist:
        print "Could not find cruise."
        context_dict["cabin_grades"] = None

    return render(request, 'cruises/cruise.html', context_dict)



def test(request):
    print "got it"
    context_dict = {}
    if request.method == "POST":
        start_date = request.POST["start"]
        start_date = datetime.strptime(start_date, '%Y-%m-%d')
        end_date = request.POST["end"]
        end_date = datetime.strptime(end_date, '%Y-%m-%d')
        print "hellO" , start_date, end_date
        cruises = Cruise.objects.filter(sail_date__range = [start_date, end_date])
        print cruises
        for cruise in cruises:
        	cruise.adults = request.POST["adults"]
        	cruise.adults = request.POST["children"]
        context_dict["cruises"] = cruises
    # cruises = Cruise.objects.filter()
    # context_dict["cruises"] = cruises
    return render(request, 'cruises/results.html', context_dict)

