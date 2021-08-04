n=int(input())
readings=[]
for i in range(n):
    readings.append(int(input()))

flat=True
increasing=True
for i in range(n-1):
    if increasing:
        if readings[i]>readings[i+1]:
            increasing=False
            flat=False
        elif readings[i]<readings[i+1]:
            flat=False

    elif not increasing:
        if readings[i]<readings[i+1]:
            flat=False
            increasing=None
            break
        elif readings[i]>readings[i+1]:
            flat=False

if flat:
    print("Fish At Constant Depth")
elif increasing==True:
    print("Fish Rising")
elif increasing==None:
    print("No Fish")
else:
    print("Fish Diving")
