import warnings
warnings.filterwarnings(action="ignore", message='the sets module is deprecated')

import phonetic
import sets
import sys
import MySQLdb
import math


def great_circle_distance(long_1,lat_1,long_2,lat_2):
    '''Returns the distance between two points on the earth.
       
    Inputs used are:
        Longitude (in radians) of the first location,
        Latitude (in radians) of the first location,
        Longitude (in radians) of the second location, and
        Latitude (in radians) of the second location.'''

    long_2=float(long_2)
    lat_2=float(lat_2)
    long_1 = math.radians(long_1)
    lat_1  = math.radians(lat_1)

    long_2 = math.radians(long_2)
    lat_2  = math.radians(lat_2)

    dlong = long_2 - long_1
    dlat = lat_2 - lat_1
    a = (math.sin(dlat / 2))**2 + math.cos(lat_1) * math.cos(lat_2) * (math.sin(dlong / 2))**2
    c = 2 * math.asin(min(1, math.sqrt(a)))
    dist = 3956 * c
    return dist * 1.609344



def fetchall(a,b):
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
        cursor.execute ("""SELECT * FROM delhi
                        """)
        while (1):
            row = cursor.fetchone ()
            if row == None:
                break
            if(great_circle_distance(a,b,row[1],row[2])) < (.400):
                break
        return row

    except MySQLdb.Error, e:
        print "Error %d: %s" % (e.args[0], e.args[1])
        sys.exit (1)

    conn.commit ()
    conn.close ()


def fetchname(a):
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
        cursor.execute ("""SELECT * FROM delhi
                        """)
        while (1):
            row = cursor.fetchone ()
            if row == None:
                break
            if(row[0]==a):
                break
        return row

    except MySQLdb.Error, e:
        print "Error %d: %s" % (e.args[0], e.args[1])
        sys.exit (1)

    conn.commit ()
    conn.close ()
	


def fetchdistance(a,b):
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
        cursor.execute ("""SELECT * FROM distance
                        WHERE ((source SOUNDS LIKE '%s' and Destination SOUNDS LIKE '%s') or (source SOUNDS LIKE '%s' and Destination SOUNDS LIKE '%s'))
                        """ % (a,b,b,a))
        row = cursor.fetchone ()
        cursor.close ()
        
    except MySQLdb.Error, e:
        print "Error %d: %s" % (e.args[0], e.args[1])
        sys.exit (1)

    conn.commit ()
    conn.close ()
    return row


    
def insertdistance(a,b,c,d,e,f,g):
    sql = "INSERT INTO distance(source, \
       destination, route, distance, averagefare, calcfare, counter) \
       VALUES ('%s', '%s', '%s', '%f', '%s', '%f', '%d' )" % \
       (a, b, c, d, e, f, g)
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
        cursor.execute (sql)
        print "Number of rows inserted: %d" % cursor.rowcount
        cursor.close ()

    except MySQLdb.Error, e:
        print "Error %d: %s" % (e.args[0], e.args[1])
        sys.exit (1)

    conn.commit ()
    conn.close ()
        

def updatedistance(a,b,c,d):
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
        cursor.execute ("""
            UPDATE distance SET averagefare = %s
            WHERE (source = %s and destination=%s) or (source =%s and destination=%s)
            """,(c,a,b,b,a))
        cursor.execute ("""
            UPDATE distance SET counter = %s
            WHERE (source = %s and destination=%s) or (source =%s and destination=%s)
            """,(d,a,b,b,a))
        print "Number of rows updated: %d" % cursor.rowcount
        cursor.close ()
    except MySQLdb.Error, e:
        print "Error %d: %s" % (e.args[0], e.args[1])
        sys.exit (1)

    conn.commit ()
    conn.close ()


# issue a statement that changes the name by including data values
# literally in the statement string, then change the name back
# by using placeholders


# create a dictionary cursor so that column values
# can be accessed by name rather than by position
def dic():
    try:
        conn = MySQLdb.connect (host = "localhost",
                                user = "root",
                                passwd = "pass123",
                                db = "temp")
    except MySQLdb.Error, e:
        print "Error %d: %s" % (e.args[0], e.args[1])
        sys.exit (1)
    try:
        cursor = conn.cursor (MySQLdb.cursors.DictCursor)
        cursor.execute ("SELECT name, longitude, latitude FROM delhi")
        result_set = cursor.fetchall ()
        for row in result_set:
            print "%s, %s, %s" % (row["name"], row["longitude"], row["latitude"])
        print "Number of rows returned: %d" % cursor.rowcount
        cursor.close ()

    except MySQLdb.Error, e:
        print "Error %d: %s" % (e.args[0], e.args[1])
        sys.exit (1)

    conn.commit ()
    conn.close ()

def avgfarecalc(userfare,avgfare,counter):
    totfare=avgfare * counter
    counter = counter + 1
    totfare = totfare + userfare
    avgfare = totfare / counter
    row= avgfare, counter
    return row


#insertdistance('akshit','nanda','halaluja',23.23,83.21,45.6,1)
#updatedistance('dwarka','rohini',98.63,8)
#a=fetchdistance('rhininew delhi','dwrkanew delhi')
#a=fetchlocationname('saket')
#b=fetchall(12.3535314,34.343424)
#updatelocation()
#dic()
#print a
#print b
#print avgfarecalc(18.0,20.0,9)
