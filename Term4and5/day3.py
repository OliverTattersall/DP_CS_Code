


def SLq9_2019(name):
    temp = []

    myfile=open(name, "r")
    count=0
    item=myfile.readline()
    while item!="":
        if len(item)==4:
            item=int(item)
            
            h = item//100
            t = (item%100)//10
            o = item%10
            print(item, h, t, o)
            if h<t and t<o:
                count+=1
                temp.append(item)
        item=myfile.readline()
    
    return temp

print(SLq9_2019("day3data.txt"))