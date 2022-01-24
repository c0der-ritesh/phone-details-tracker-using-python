
from unittest import result
import phonenumbers
import folium
import opencage
from phonenumbers import timezone,geocoder,carrier
number=input("enter your phone number with +_ _: ")
phone=phonenumbers.parse(number)
time=timezone.time_zones_for_number(phone)
car=carrier.name_for_number(phone,"en")
location=geocoder.description_for_number(phone,"en")
print(phone)
print(time)
print(car)
print(location)
from opencage.geocoder import OpenCageGeocode
key='67c6886220a341f9b0f54a331c5cdae2'
geocoder=OpenCageGeocode(key)
query=str(location)
results=geocoder.geocode(query)
#print(results)
lat =results[0]['geometry']['lat']
lng =results[0]['geometry']['lng']
print(lat,lng)
myMap=folium.Map(location=[lat,lng],zoom_start=9)
folium.Marker([lat,lng],popup=location).add_to(myMap)

myMap.save("mylocation.html")