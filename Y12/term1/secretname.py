print("code to create your codename")

name = list(input("name: ").lower())

for i in range(0, len(name), 2):
    name[i], name[i+1] = name[i+1], name[i]

print("spy name: "+''.join(name))

