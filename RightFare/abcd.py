import warnings
warnings.filterwarnings(action="ignore", message='the sets module is deprecated')

import urllib
import sys
import re
import simplejson
import MySQLdb

def fetchpincode(a):
    try:
        conn = MySQLdb.connect (host = "localhost",
                                user = "root",
                                passwd = "pass123",
                                db = "temp")
    except MySQLdb.Error, e:
        print "Error %d: %s" % (e.args[0], e.args[1])
        sys.exit (1)
    try:
        cursor = conn.cursor ()
        cursor.execute ("""SELECT * FROM pin
                        WHERE (pincode=%s)
                        """,(a))
        row = cursor.fetchone ()
        print row
        print "Number of rows returned: %d" % cursor.rowcount
        cursor.close ()
        
    except MySQLdb.Error, e:
        print "Error %d: %s" % (e.args[0], e.args[1])
        sys.exit (1)

    conn.commit ()
    conn.close ()
    return row
    
def rem_least(list1):
    if list1==[]:
        return list1
    max_ctr=list1.count(list1[0])
    x=len(list1)
    i=0
    list3=[]
    while i<x:
        if(list1.count(list1[i])>max_ctr):
            mx_ctr=list1.count(list1[i])
            #i=0
            continue
        i=i+1
    i=0
    x=len(list1)
    print max_ctr
    while i<x:
        x=len(list1)
        if(list1.count(list1[i])<max_ctr):
            j=i
            i=0
            list1.pop(j)
            continue

        i=i+1
    return list1
def final(list1):
    if list1==[]:
        return list1
    a=len(list1)
    i=0
    while (a>=1 and i<a):
        if (list1[i] in list1[i+1:]):
            list1.pop(i)
            a=a-1
        else:
            i=i+1
    return list1

def google_results(search_query):
  query = urllib.urlencode({'q' : search_query})
  url_list=[]
  url=[]
  url = 'http://ajax.googleapis.com/ajax/services/search/web?rsz=large&start=0&v=1.0&%s'% (query)
  search_results = urllib.urlopen(url)
  json = simplejson.loads(search_results.read())
  results = json['responseData']['results']
  for i in results:
    url_list.append(i['url'])
  return url_list
def new(y):
  x= google_results(y) 
  print x
  list3=[]
  i=0
  for i in x:
    print i
    page=urllib.urlopen(i)
    pagedata = page.read()
    pin='1100[0-9][0-9]'
    list2=re.findall(r'\b'+pin,pagedata)
    for j in list2:
      list3.append(j)
  #if (list3==[]):
  #    print 'No such place found'
  print list3
  print '\n'
  tlist=rem_least(list3)
  print tlist
  print '\n'
  flist=final(tlist)
  if flist==[]:
      return '' #Returns empty string as  address not found !
  print "final list is"
  print flist
  for i in flist:
    x=fetchpincode(i)
    if (x!=None):
        l=x[1].rsplit(',')
        return l[0]
    else:
        print "no such pincode"


#new('Yamuna Old Bridge, New Delhi, Delhi')
