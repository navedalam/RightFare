import userfare
import sample1
def store(l):#l contains no, src, dest
    #l[1]=l[1]+"New Delhi"
    #l[2]=l[2]+"New Delhi"
    x=sample1.fetchdistance(l[1],l[2])
    if(x!=None):
        print "given strings in database"
        userfare.insert(l[0],x[0],x[1])
    else:
        userfare.insert(l[0],l[1],l[2])

def updateuserfare(l):#l contains no, userfare
    y=userfare.fetchvalues(l[0])
    print y
    z=[]
    z.append(y[1])
    z.append(y[2])
    return z

'''l=['919968379126','anand vihar','patparganj']
store(l)
l=['919968379126','150']
z=updateuserfare(l)
print z'''
