import os
import read
import sms_read
import RightFare
import useravg
l=[]
for filename in os.listdir('C:\Users\DELL\Desktop\Source Code_Complete Rightfare\Version 0.0\sms gateway files'):
    l.append(filename)
print l
dirname='C:\\Users\\DELL\\Desktop\\Source Code_Complete Rightfare\\Version 0.0\\sms gateway files\\'
print dirname
for i in l:
    print i
    name=os.path.join(dirname,i)
    print name
    l1 = read.fileread(name)
    print l1
    x = sms_read.checker(name)
    if (x==1):
        RightFare.rf(l1)
    if (x==2):
        l1.pop(0)
        useravg.callavg(l1)
        
        
