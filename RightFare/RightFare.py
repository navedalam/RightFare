import abcd
import wikimapia
import googlemaps
import rightfare_func
import sample1
import sys
import multiquery
from googlemaps import GoogleMaps
gmaps = GoogleMaps('ABQIAAAAU6aB_SumFVXY8JuehQcWXRRPdrwtlRIZKQUOo_MxBO_KFxU4HhRWfVQKeLerXiLRHZpWt_AaKWWZIg') #calls google maps with the API Key required

def findlocpin(l):
    pincode=abcd.new(l)
    if(pincode==None):
        return None
    l=pincode[0]
    latlng=gmaps.address_to_latlng(l)
    return latlng
def geocode(add):
    x=sample1.fetchname(add)
    if (x!=None):
        return x
    add=add+'New Delhi'
    x=gmaps.address_to_latlng(add)
    if(x[0]!=28.635308 and x[1]!=77.22496):
        return x
    print 'Not Found On Google Maps'
    x=wikimapia.wiki(add)
    if(x!=(0,0)):

        return x
    print "Not Found on Wikimapia"
    return 0
def findpincode(add):
    x=findlocpin(add)
    if(x!=()):
        return x
    print "Not found Address"+ add
    return 0
def checker(l):
    list_values=[]
    flag1=0
    flag2=0
#    f1=0
#    f2=0
    list_values=l
    x=sample1.fetchdistance(list_values[1],list_values[2])
    if(x!=None):
        print "given strings in database"
        fare = x[5]
        avg_fare = x[4]
        distance = x[3]
        imp_waypoints = x[2]
        counter = x[6]
        rightfare_func.get_file(fare,avg_fare,list_values[0],list_values[1],list_values[2],distance,imp_waypoints)
        sys.exit()
    a=geocode(list_values[1])
    b=geocode(list_values[2])
    if(a==0):
        print "Checked pin code for a"
        findpincode(a)
    if b==0:
        print "Checked pin code for b"
        findpincode(b)
    if(a==0) or (b==0):
        sys.exit()
        
    #x=sample.fetchdistancelatlng(a,b)#this function has to be written
    '''if(x!=None):
        print "given strings in database"
        fare = x[5]
        avg_fare = x[4]
        distance = x[3]
        imp_waypoints = x[2]
        counter = x[6]
        rightfare_func.get_file(fare,avg_fare,list_values[0],list_values[1],list_values[2],distance,imp_waypoints)
        sys.exit()'''
    #else:
    return a[0],a[1],b[0],b[1]
def rf(l):
    imp_waypts=[] 
    listimp=[]
    a=''
    b=[]
    i=0
    flag=0
    route_list=[] 
    list_values=[] 
    lat_a=0.0
    lat_d=0.0
    lng_a=0.0
    lng_d=0.0
    lat_a,lng_a,lat_d,lng_d = checker(l)
    list_values = l
    address = gmaps.latlng_to_address(lat_a,lng_a)
    print address
    destination = gmaps.latlng_to_address(lat_d,lng_d)
    print destination
    directions = gmaps.directions(address, destination)
    for step in directions['Directions']['Routes'][0]['Steps']:
        a=step['descriptionHtml']
        route_list.append(a)
    print '\n\n****Route Calculated****\n\n'
    route_distance=0.0
    route_distance= (directions['Directions']['Distance']['meters']/1000.0)
    print 'Total Distance is :',route_distance,'km'
    route_time=0.0
    route_time=(directions['Directions']['Duration']['seconds']/60.0)
    print 'Total Time is :',route_time,'min'
    i=0
    for i  in route_list:
        rightfare_func.keywrd_lift(i)
    rightfare_func.keywrd_remove()
    imp_waypts=rightfare_func.giv_value()
    print '\n\nThe Route to be Followed is \n\n:'
    rightfare_func.print_route(route_list)
    imp_waypts = rightfare_func.red(imp_waypts)
    print '\n\n****Important Waypoints****\n\n'
    for i in imp_waypts:
        print i
    fare=rightfare_func.calc_fare(route_distance)
    print "\n\n\n Total fare is: ",fare
    rightfare_func.file_avg(list_values[1],list_values[2])
    rightfare_func.get_file(fare,'0',list_values[0],list_values[1],list_values[2],route_distance,imp_waypts)
    str_waypts=rightfare_func.cnvrt(imp_waypts)
    src=list_values[1][:-9]
    dst=list_values[2][:-9]
    sample1.insertdistance(src,dst,str_waypts,route_distance,'0',fare,0)
l=['919711085518','asd','asd']
rf(l)
