def findPrimes(n):
    primes=[]
    prime = [True for _ in range(n+1)]

    p=2
    while p**2<=n:
        if prime[p]:
            for i in range(p**2, n+1, p):
                prime[i]=False
        p+=1
    
    for i in range(2, n+1, 1):
        if prime[i]:
            primes.append(i)
    return primes






def isSemiprime(n):
    primes=findPrimes(n)

    result = False
    for i in range(len(primes)):

        if n%primes[i]==0:
            item = n//primes[i]

            for j in range(len(primes)):

                if item%primes[j]==0:
 
                    if item//primes[j]==1:
                        result=True

    return result
answer=[4, 6, 9, 10, 14, 15, 21, 22, 25, 26, 33, 34, 35, 38, 39, 46, 49, 51, 55, 57, 58, 62, 65, 69, 74, 77, 82, 85, 86, 87, 91, 93, 94, 95]
test=[i for i in range(100)]
for i in range(100):
    if isSemiprime(i):
        print(i)
print(isSemiprime(1829))
# print(answer)

def isSuperPrime(n):
    primes = findPrimes(n)
    # print(primes)
    result=False
    if primes[-1]==n:
        for j in range(len(primes)):

            if primes[j]==len(primes):

                result=True


    return result

# print(isSuperPrime(11))



# print(findPrimes(100))