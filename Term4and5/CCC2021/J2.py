n = int(input())

names=[]
bids=[]

for i in range(n):
    names.append(input())
    bids.append(int(input()))

max=float('-inf')
check=0
for i in range(n):
    
    if bids[i]>max:

        max=bids[i]
        check=i

print(names[check])