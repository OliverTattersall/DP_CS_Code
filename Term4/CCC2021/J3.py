go = []
steps=[]

temp = input()
while temp!="99999":
    go.append(temp[0:2])
    steps.append(int(temp[2:]))
    temp=input()

rules=[]
for i in range(len(go)):
    sum=0
    for j in range(2):
        sum+=int(go[i][j])

    if sum==0:
        rules.append(rules[-1])
    elif sum%2==0:
        rules.append("right")

    else:
        rules.append("left")

for i in range(len(steps)):
    print(rules[i], " ", steps[i])