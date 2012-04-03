import sample1
import multiquery
def callavg(l):#l contains no,userfare
    list3=[]
    list1=multiquery.updateuserfare(l)
    source=list1[0]+"New Delhi"
    print source
    destination=list1[1]+"New Delhi"
    print '******'
    print destination
    print '******'
    avgfare=float(l[1])
    print avgfare
    print type(avgfare)
    list2=sample1.fetchdistance(source,destination)
    print list2
    value=float(list2[4])

    counter=int(list2[6])
    print counter
    print type(counter)
    print '******'
    list3=sample1.avgfarecalc(avgfare,value,counter)
    print list3
    avgfare=str(list3[0])
    print type(avgfare)
    counter=int(list3[1])
    print type(counter)
    counter=str(counter)
    print type(counter)
    sample1.updatedistance(source,destination,avgfare,counter)
l=['919711085518','70.33']
#for i in sys.argv():
 #   l.append(i)
#l.pop(0)
callavg(l)
