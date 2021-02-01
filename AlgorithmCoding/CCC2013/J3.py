year=int(input())

test=True
while test:
    year+=1
    temp=list(str(year))
    temp2=list(set(temp))
    temp.sort()
    temp2.sort()
    if temp == temp2:
        test=False


    
print(year)