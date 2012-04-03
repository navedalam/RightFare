import urllib
def remov(list3,list4):
    list1=[]
    list2=[]
    for i in list3:
        list1.append(int(i))
    for i in list4:
        list2.append(int(i))
    def rem_least(list1):
        max_ctr=list1.count(list1[0])
        x=len(list1)
        i=0
        list3=[]
        list4=[]
        while i<x:
            if (list1.count(list1[i])<max_ctr):
                y=list1[i]
                list3.append(y)
            elif(list1.count(list1[i])>max_ctr):
                max_ctr=list1.count(list1[i])
                i=0
                continue
            i=i+1
 

        x=len(list3)
        i=0
        while  i<x:
            list4.append(list1.index(list3[i]))
            list1[list1.index(list3[i])]=list1[list1.index(list3[i])]+1
            i=i+1
        return list4
    x1=rem_least(list1)
    x2=rem_least(list2)
    for i in x2:
       if i not in x1:
            x1.append(i)
    x1.sort()
    return x1
     
def getlong(test):
    b='</lon>'
    x=len(test)
    i=5
    f=''
    while(i<x-5):
       if (b==test[i:i+6]):
           break
       f=f+test[i]
       i=i+1
    return f
def getlat(test):
    b='</lat>'
    x=len(test)
    i=26
    f=''
    while(i<x-5):
       if (b==test[i:i+6]):
           break
       f=f+test[i]
       i=i+1
    return f
def rem_space(string1):
    l=string1.rsplit(' ');
    f=l[0]
    
    for i in range(1,len(l)):
        f='%20'+f+'%20'+l[i]
    return f
def wiki(query):
    query=rem_space(query)
    #query=query+'%20New%20Delhi'
    x='http://api.wikimapia.org/?function=search&key=C962EFD6-5BE5C6C5-C6542EBA-DC19BB56-C3A33AA0-04BAE3EC-6DCB3BE0-CC94A576&q='
    x=x+query
    page = urllib.urlopen(x)
    pagedata = page.read()
    #print pagedata
    l=pagedata.rsplit('\n')
    first=l[2]
    l1=first.rsplit('<location>')
    #print l1
    l1.pop(0)
    #print l1
    lon=[]
    lat=[]
    for i in l1:
        lon.append(getlong(i))
        lat.append(getlat(i))
    lon1=[]
    lat1=[]
    for i in lon:
        i=i.rsplit('.')
        lon1.append(i[0])
    for i in lat:
        i=i.rsplit('.')
        lat1.append(i[0])
    if (lat1==[]) or (lon1==[]): #(0,0) as a return from wikimapia signifies no result
        return 0,0
    x=remov(lon1,lat1)
    counter=0
    for i in x:
        lat.pop(i-counter)
        lon.pop(i-counter)
        counter=counter+1
    return lat[0],lon[0]

