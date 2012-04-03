import os
import sys
def checker(name):
    if(os.path.isfile(name)):
        fout = open(name,'r')
        list1=fout.readlines()
        fout.close()
        print list1
        #print len(list1)
        if (list1[8][0:3]=='RF1'):
            print 'check'
            return 1
        elif (list1[8][0:3]=='RF2'):
            print 'avg'
            return 2
        else:
            print 'no'
        #sys.exit()
    else :
        print 'NO such File'
        #checker()

