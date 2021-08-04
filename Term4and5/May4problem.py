def factorize(n):
    factors = set()

    for i in range(1, int(n**(1/2))+1, 1):
        if n%i==0:
            factors.add(n//i)
            factors.add(i)

    factors=sorted(factors)
    return factors

print(factorize(10))


def factor(n, count):
    if count>(int(n**(1/2)))+1:
        return ""
    ans=""
    if n%count==0:
        ans= str(count)+" " + str(n//count)+" "
    return factor(n, count+1)+ans

print(sorted(set(factor(16, 1).split()), key = lambda x:int(x)))