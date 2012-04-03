import googlemaps
from googlemaps import GoogleMaps
gmaps = GoogleMaps('ABQIAAAAU6aB_SumFVXY8JuehQcWXRRPdrwtlRIZKQUOo_MxBO_KFxU4HhRWfVQKeLerXiLRHZpWt_AaKWWZIg') #calls google maps with the API Key required
x=gmaps.address_to_latlng('dsa new delhi')
y=gmaps.latlng_to_address(x[0],x[1])
print x
print y
