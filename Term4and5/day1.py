def sumit(dct):
    lst= list(dct.keys())
    sum=0
    for i in lst:

        if type(dct[i])!=str:
            sum+=dct[i]

    return sum


dct={"a":3, "b":43.6, "c":"sda"}

print(sumit(dct))