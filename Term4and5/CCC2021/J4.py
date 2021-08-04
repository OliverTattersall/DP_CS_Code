og = list(input())

def swap(lst, i, j):
    a = lst[i]
    b = lst[j]

    lst[i]=b
    lst[j]=a

    return lst

# print(og)

brokenL=False
brokenS=False
min=0
max=len(og)
for i in range(len(og)):
    if brokenL!=True:
        if og[i]!="L":
            brokenL=True
        else:
            min+=1
            # og.pop(0)
    if brokenS!=True:
        if og[len(og)-1-i]!="S":
            brokenS=True
        else:
            # og.pop(-1)
            max-=1
og=og[min:max]
# print(og)
count=0
for i in range(1, len(og),1):
    if og[i]=="L":
        k=i
        while k!=0 and og[k-1]!="L":
            # print(k)
            og = swap(og, k-1, k)
            count+=1
            k-=1
    if og[len(og)-i-1]=="S":
        k=i
        while k!=len(og)-1 and og[k+1]!="S":
            og = swap(og, k, k+1)
            count+=1


print(count)