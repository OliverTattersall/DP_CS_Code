# N=int(input())
# people=[]
# cons={"m":1, "dm":0.1, "cm":0.01, "mm":0.001}

# for i in range(N):
#     people.append(input().split())

myfile=open("data.txt", "r")
item=myfile.read().split("\n")
N=int(item[0])
people=[]

for i in range(1, N+1):
    people.append(item[i].split())

cons={"m":1, "dm":0.1, "cm":0.01, "mm":0.001}
myfile.close()


for i in range(N):
    people[i][1]=float(people[i][1])*cons[people[i][2]]

people.sort(key = lambda x:x[1])
# print(people)

for i in range(N-1, N-6, -1):
    print(people[i][0])