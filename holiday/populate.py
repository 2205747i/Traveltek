import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'holiday.settings')
import django
django.setup()
import requests
from lxml import etree
from cruises.models import Cruise
from datetime import datetime



testreq = '''<?xml version="1.0"?>
<request>
 <auth username="hackathon" password="pr38ns48" />
 <method action="simplesearch" sitename="cruisedemo.traveltek.net"
 status="Live" type="cruise">
 <searchdetail 
 	type="cruise" startdate="2017-04-01" enddate="2017-04-03"
	adults="2" children="0" sid="30115" resultkey="default">
 </searchdetail>
 </method>
</request>'''

print(testreq)

r = requests.post('https://fusionapi.traveltek.net/0.9/interface.pl', data = {"xml": testreq})
root = etree.fromstring(r.text)
print r.text
for element in root.iterfind("results/cruise"):
    id = element.get("codetocruiseid")
    nights = element.get("nights")
    name = element.get("name")
    sail_nights = element.get("sailnights")
    sail_date = element.get("saildate")
    print ("id: {0}, nights: {1}, name: {2}, sail_nights: {3}, sail_date: {4}".format(id, nights,name,sail_nights, sail_date))
    c = Cruise.objects.get_or_create(code_to_cruise_id = id, sail_date = datetime.now())[0]
    c.nights = nights
    c.name = name
    c.sail_nights = sail_nights
    c.sail_date = sail_date
    print("sdfd ", c)
    c.save()
    print c.name

