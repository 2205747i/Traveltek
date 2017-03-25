import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'holiday.settings')
import django
django.setup()
import requests
from lxml import etree
from cruises.models import Cruise



testreq = '''<?xml version="1.0"?>
<request>
 <auth username="hackathon" password="pr38ns48" />
 <method action="simplesearch" sitename="cruisedemo.traveltek.net"
 status="Live" type="cruise">
 <searchdetail 
 	type="cruise" startdate="2017-04-01" enddate="2017-04-30"
	adults="2" children="0" sid="30115" resultkey="default">
 </searchdetail>
 </method>
</request>'''

print(testreq)

r = requests.post('https://fusionapi.traveltek.net/0.9/interface.pl', data = {"xml": testreq})
root = etree.fromstring(r.text)
for element in root.iterfind("results/cruise"):
    id = element.get("codetocruiseid")
    c = Cruise.objects.get_or_create(code_to_cruise_id = id)
    nights = element.get("nights")
    c.nights = nights
    name = element.get("name")
    c.name = name
    sail = element.get("sailnights")
    c.sail_nights = sail
    date = element.get("saildate")
    c.sail_date = date
    c.save()
    print(c)


