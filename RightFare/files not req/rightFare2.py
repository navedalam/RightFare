import googlemaps
import rightfare_func
import sample1
import sys
#import smstest
from googlemaps import GoogleMaps
gmaps = GoogleMaps('ABQIAAAAU6aB_SumFVXY8JuehQcWXRRPdrwtlRIZKQUOo_MxBO_KFxU4HhRWfVQKeLerXiLRHZpWt_AaKWWZIg') #calls google maps with the API Key required

def read_file():
    fout = open('C:\Users\DELL\Desktop\GSM1.XX3hvcuE','r')
    list2=[]
    list3=[]
    list1=fout.readlines()
    fout.close()
    list2.append(list1[1])
    list2.append(list1[8])
    print list2
    list3.append(list2[0][10: ])
    list3.append(list2[1][5: ])
    list3[1]=list3[1].rsplit(',')
    list3.extend(list3[1])
    list3.pop(1)
    print list3
    print list3
    return list3
#variable definition here

def checker():
    list_values=[]
    list_values=read_file()
    x=sample1.fetchdistance(list_values[1],list_values[2])
    if(x!=None):
        print "given strings in database"
        fare = x[5]
        avg_fare = x[4]
        distance = x[3]
        imp_waypoints = x[2]
        #n = len(imp_waypts)
        #for i in range(0,n):
        #    imp_waypts[i]=rightfare_func.rem_vowels1(i)
        #print imp_waypts
        counter = x[6]
        rightfare_func.get_file(fare,avg_fare,list_values[0],list_values[1],list_values[2],distance,imp_waypoints)
        #sample1.updatedistance(list_values[1],list_values[2],avg_fare,counter)
        sys.exit()
    list_values[1]= list_values[1]+ 'New Delhi'
    lat_a,lng_a = gmaps.address_to_latlng(list_values[1])
    list_values[2]= list_values[2]+ 'New Delhi'
    lat_b,lng_b = gmaps.address_to_latlng(list_values[2])
    a=sample1.fetchall(lat_a,lng_a) 
    b=sample1.fetchall(lat_b,lng_b) 
    if(a!=None and b!=None):
        print "given string in database"
        x = sample1.fetchdistance(a[0],b[0])
        fare = x[5]
        avg_fare = x[4]
        distance = x[3]
        imp_waypoints = x[2]
        rightfare_func.get_file(fare,avg_fare,list_values[0],list_values[1],list_values[2],distance,imp_waypoints)
        sys.exit()
    return lat_a,lng_a,lat_b,lng_b


imp_waypts=[] # Will hold the Important waypoints from my Route List
listimp=[]

a=''
b=[]
i=0
flag = 0
route_list=[] # Holds the fetched data about the route
list_values=[] #holds the values to be input in sequence from number , source , destination
lat_a=0.0#lat of address
lat_d=0.0#lat of destination
lng_a=0.0
lng_d=0.0
lat_a,lng_a,lat_d,lng_d = checker()
#variable definition ends

list_values = read_file()
address = list_values[1]
destination = list_values[2]

#lat_a,lng_a = gmaps.address_to_latlng(address)
#print lat_a,lng_a
address = gmaps.latlng_to_address(lat_a,lng_a)
print address
#destination = destination + ',New Delhi ,India'
#lat_d,lng_d = gmaps.address_to_latlng(destination)
#print lat_d,lng_d
destination = gmaps.latlng_to_address(lat_d,lng_d)
print destination
directions = gmaps.directions(address, destination)
print directions

for step in directions['Directions']['Routes'][0]['Steps']:
    a=step['descriptionHtml']
    route_list.append(a)
#for i in listtemp:
#    print i
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
#imp_waypts=rightfare_func.giv_value()
#for i in imp_waypts:
 #   print i
#rightfare_func.remove_doubling()
imp_waypts=rightfare_func.giv_value()
print '\n\nThe Route to be Followed is \n\n:'
rightfare_func.print_route(route_list)
print '\n\n****Important Waypoints****\n\n'
for i in imp_waypts:
    print i
fare=rightfare_func.calc_fare(route_distance)
print "\n\n\n Total fare is: ",fare
rightfare_func.file_avg(list_values[1],list_values[2])
imp_waypts = rightfare_func.red(imp_waypts)
n = len(imp_waypts)
for i in range(0,n):
    imp_waypts[i]=rightfare_func.rem_vowels1(imp_waypts[i])
print imp_waypts
rightfare_func.get_file(fare,'0',list_values[0],list_values[1],list_values[2],route_distance,imp_waypts)
str_waypts=rightfare_func.cnvrt(imp_waypts)
sample1.insertdistance(list_values[1],list_values[2],str_waypts,route_distance,'0',fare,0)
