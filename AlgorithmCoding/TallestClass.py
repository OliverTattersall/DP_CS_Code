# N=int(input())
# people=[]
# cons={"m":1, "dm":0.1, "cm":0.01, "mm":0.001}

# for i in range(N):
#     people.append(input().split())

myfile=open("data.txt", "r")

item=myfile.read()
# print(item)
item=item.split("\n")
# print(item)
myfile.close()

N=int(item[0])
people=[]

for i in range(1, N+1):

    people.append(item[i].split())

# for r in range(0, len(people), 1):
#     print(people[r])

cons={"m":1, "dm":0.1, "cm":0.01, "mm":0.001}

# converting everything to meters 
for i in range(N):
    people[i][1]=float(people[i][1])*cons[people[i][2]]

people.sort(key = lambda x:x[1])


# people = sorted(people)

for i in range(N-1, N-6, -1):
    print(people[i][0])