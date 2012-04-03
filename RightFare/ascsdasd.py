import warnings
warnings.filterwarnings(action="ignore", message='the sets module is deprecated')

import phonetic
import sets
import sys
import MySQLdb
import math



    


def fetchdistance(a,b,c):
    sql = "INSERT INTO timetest(number, \
       source, destination) \
       VALUES ('%s', '%s', '%s' )" % \
       (a, b, c)
    try:
        conn = MySQLdb.connect (host = "localhost",
                                user = "root",
                                passwd = "pass123",
                                db = "sample")
    except MySQLdb.Error, e:
        print "Error %d: %s" % (e.args[0], e.args[1])
        sys.exit (1)
    try:
        cursor = conn.cursor ()
        cursor.execute (sql)        
        cursor.execute (""" SELECT time FROM timetest
                        WHERE number= '%s' and source= '%s' and destination= '%s'
                        """ % (a,b,c))
        d = cursor.fetchone()
        print "a"
        d = d[0]
        while(1):
            cursor.execute ("""SELECT * FROM timetest
                            """)
            row = cursor.fetchone ()
            print "a"
            x=row[4]
            cursor.execute ("""SELECT TIMEDIFF('%s','%s')
                            """ % (d,x))
            z=cursor.fetchone()
            z=z[0]
            print "a"
            z=str(z)
            z=z.split(':')
            z[0]=int(z[0])
            if z[0]>23:
                cursor.execute(""" DELETE from timetest
    `   `                      WHERE number = '%s' and source = '%s' and destination = '%s'
                               """ % (row[1],row[2],row[3])) 
            else:
                break
            cursor.close ()
        
    except MySQLdb.Error, e:
        print "Error %d: %s" % (e.args[0], e.args[1])
        sys.exit (1)

    conn.commit ()
    conn.close ()
    

    
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

#insertdistance('akshit','nanda','halaluja',23.23,83.21,45.6,1)
#updatedistance('dwarka','rohini',98.63,8)
fetchdistance("9378930938","silchar","guwahati")
#a=fetchlocationname('saket')
#b=fetchall(12.3535314,34.343424)
#updatelocation()
#dic()
#print x
#print b
#print avgfarecalc(18.0,20.0,9)
