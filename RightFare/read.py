#fout = open('C:\Users\DELL\Desktop\WinRAR_3.80_Professional\GSM1.XX3hvcuE','r')
def fileread(name):
    fout = open(name,'r')
    list2=[]
    list3=[]
    list1=fout.readlines()
    fout.close()
    list2.append(list1[1])
    list2.append(list1[8])
    print list2
    list3.append(list2[0][10: ])
    list3.append(list2[1][5: ])

    list3[1]=list3[1].rsplit(',')
    list3.extend(list3[1])
    list3.pop(1)
    print list3
    return list3

