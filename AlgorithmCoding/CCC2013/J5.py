#incomplete


team=int(input())
n=int(input())
results=[]

x=set([])
for i in range(1, 5):
    for j in range(1, 5):
        if i!=j:
            if (i, j) not in x and (j, i) not in x:
                x.add((i, j))

for i in range(n):
    temp=input().split()
    for j in range(4):
        temp[j]=int(temp[j])

    results.append(temp)
    if (temp[0], temp[1]) in x:
        x.remove((temp[0], temp[1]))
    if (temp[1], temp[0]) in x:
        x.remove((temp[1], temp[0]))

games={ i : 0 for i in range(1, 5)}
scores={ i : 0 for i in range(1, 5)}


for i in range(n):
    temp=results[i]
    games[temp[0]]+=1
    games[temp[1]]+=1
    if temp[2]>temp[3]:
        scores[temp[0]]+=3
    elif temp[2]==temp[3]:
        scores[temp[0]]+=1
        scores[temp[1]]+=1
    else:
        scores[temp[1]]+=3

print(games, scores)

count = 0
numgamesleft=6-n
print(x)





    