vals=input().split()
for i in range(4):
    vals[i]=float(vals[i])

r2=(vals[2]-vals[0])**2 + (vals[3]-vals[1])**2

a=3.14159*r2
print(a)