n=int(input())

matrix=[]

for i in range(n):
    temp=input().split()
    for j in range(n):
        temp[j]=int(temp[j])
    matrix.append(temp)

magic = sum(matrix[0])
answer="magic"

for i in range(n):
    sum1=0
    sum2=0
    for j in range(n):
        sum1+=matrix[i][j]
        sum2+=matrix[j][i]

    if sum1!=magic or sum2!=magic:
        answer="not magic"

print(answer)
