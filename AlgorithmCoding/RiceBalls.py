#incomplete

N=int(input())
balls=input().split()
for i in range(N):
    balls[i]=int(balls[i])

test=True
temp=[]
while test:
    print(balls)
    temp=[]
    i=0
    count=0
    while i<len(balls):
        tempval=i
        if i<= len(balls)-2:
            if balls[i]==balls[i+1]:
                temp.append(balls[i]+balls[i+1])
                i+=1
                count+=1

        if i<=len(balls)-3:
            if balls[i]==balls[i+2]:
                temp.append(balls[i]+balls[i+1] + balls[i+2])
                i+=2
                count+=1

        if tempval==i:
            temp.append(balls[i])
        i+=1
    balls=temp
    if count==0:
        test=False

print(max(balls))