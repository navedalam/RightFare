import warnings
warnings.filterwarnings(action="ignore", message='the sets module is deprecated')

import sets
import sys
import MySQLdb
import math


def insert(a,b,c):
    sql = "INSERT INTO userfare(phne_no, \
       source, destination) \
       VALUES ('%s', '%s', '%s')" % \
       (a, b, c)
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

def fetchvalues(a):
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
        cursor.execute ("""SELECT * FROM userfare
                        WHERE phne_no = %s
                        """, (a))
        row = cursor.fetchone ()
        z=row
        return z
        print "Number of rows returned: %d" % cursor.rowcount
        cursor.close ()
    except MySQLdb.Error, e:
        print "Error %d: %s" % (e.args[0], e.args[1])
        sys.exit (1)

    conn.commit ()
    conn.close ()
    
#print fetchvalues('919711085518')
