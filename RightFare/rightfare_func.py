import googlemaps
import rightfare_func
from googlemaps import GoogleMaps
import sample1
gmaps = GoogleMaps('ABQIAAAAU6aB_SumFVXY8JuehQcWXRRPdrwtlRIZKQUOo_MxBO_KFxU4HhRWfVQKeLerXiLRHZpWt_AaKWWZIg') #calls google maps with the API Key required
imp_waypts=[]
listimp=[]
templist=[]
def calc_fare(distance):# calculates the meter fare based on distance
    distance = distance-1
    fare=19.65
    distance = distance /0.1
    x= distance * .65
    fare = fare + x
    return fare
def keywrd_lift(string1):  # Lifts Important keywords from the Route
    a=string1
    b='<b>'
    c='</b>'
    i=0
    ctr =0
    f=''
    while(i<(len(a)-2)):
        if(b==a[i:i+3]):
            ctr=1
            i=i+3
            continue
        if(c==a[i:i+4]):
            ctr=2
            i=i+4
            imp_waypts.append(f)
            f=''
            continue
        if(ctr==1):
            f=f+a[i]
        i=i+1
def keywrd_remove():  #
    checker=[u'right',u'left',u'west',u'east',u'north',u'south','',u'southeast',u'southwest',u'northeast',u'norhtwest','1st','2nd','3rd','4th','5th','6th','7th','8th','9th']
    i=0
    x=len(imp_waypts)
    while (i<x):
        x=len(imp_waypts)
        if(imp_waypts[i]in checker):
            imp_waypts.pop(i)
            i=0
        i=i+1
    for i in imp_waypts:
        if(i in templist):
            continue
        else:
            templist.append(i)

def rem_nbsp(a):
    b='&nbsp;'
    i=0
    f=''
    while(i<(len(a))):
          if(b==a[i:i+6]):
              i=i+6
              continue
          f=f+a[i:i+1]
          i=i+1
    return f

def rem_wbr(a):
    b='<wbr/>'
    i=0
    f=''
    while(i<(len(a))):
          if(b==a[i:i+6]):
              i=i+6
              continue
          f=f+a[i:i+1]
          i=i+1
    return f

def print_route(listt): #Print the route from the fetched data , different from removing kewords
    flag=0

    for i in listt:
        a =''
        for ch in i:
            if(ch == '<'):
                flag = 1
            if(ch == '>'):
                flag = 0
                continue
            if(flag == 0):
                #b.append(ch)
                a=a+ch
        
        listimp.append(a)
    for i in listimp:
        i=rem_nbsp(i)
    for i in listimp:
        i=rem_wbr(i)
        print i
    
'''def remove_doubling():
    #i=len(imp_waypts)-1
    #while(i>=0):
     #   if(imp_waypts[i] in imp_waypts[0:i]):
      #      imp_waypts.pop(i)
       #     i=i-2
        #else :
         #   i=i-1
    templist=[]
    for i in imp_waypts:
        if(i in templist):
            continue
        else:
            templist.append(i)
    imp_waypts=templist'''

def giv_value():
    return templist

def rem_vowels1(str1):
    n = len(str1)
    str2=''
    
    vow=['a','e','i','o','u']
    for i in range(0,n-1):
        flag=0
        for j in vow:
            if(str1[i]==j):
                flag=1
        if(flag==0):
            str2=str2+str1[i]
    str2=str2+str1[n-1]
    return str2
    
def cnvrt(waypts):
    b=''
    i=0
    for  i in waypts:
        b=b+i+' '
    return b

def get_input(directions):
    direct=directions
    print direct
def file_avg(add,dest):
    fout=open('avg.txt','w')
    fout.write(add+u"\n")
    fout.write(dest+u"\n")
    fout.close()
def red(list1):
    x= len(list1)
    list2=[]
    z=0
    if(x>7):
        z=x/2
        list2.append(templist[z-2]+u"\\")
        list2.append(templist[z]+u"\\")
        list2.append(templist[z+2]+u"\\")
    elif(x<7)and(x>3):
        z=x/2
        list2.append(templist[z-1]+u"\\")
        list2.append(templist[z]+u"\\")
        list2.append(templist[z+1]+u"\\")
    else:
        for i in templist:
            list2.append(i+u"\\")
    return list2

def get_file(fare,avg_fare, number,add,dest,dist,route):
    add=add[:-9]
    dest=dest[:-9]
    fout=open("Rightfare_result.txt","w")
    fout.write("To : ")
    fout.write(number + u"\n")
    #fout.write("Source :")
    fout.write(add + u"/")
    #fout.write("Destination :")
    fout.write(dest + u"\n")
    fout.write("Mtr:")
    fare = str(fare)
    fout.write(fare + u"\n")
    fout.write("Avg:")
    avg_fare = str(avg_fare)
    fout.write(avg_fare + u"\n")
    fout.write("Dist:")
    dist = str(dist)
    fout.write(dist + u"\n")
    fout.write("Path:")
    for i in route:
        fout.write(i+u"\n")
    fout.close()
    #return ("Rightfare_result.txt")
