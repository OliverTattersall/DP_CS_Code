weight=int(input())

n=int(input())
chores=[]

for i in range(n):
    chores.append(int(input()))

chores.sort()

count=0
i=0
while weight>0 and i<n:
    if weight-chores[i]>=0:
        count+=1
        weight = weight - chores[i]
    else:
        weight=0

    i+=1

print(count)
