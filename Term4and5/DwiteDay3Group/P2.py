
def findPrimes(n): 
    primes=[]
    prime = [True for i in range(n+1)] 

    p = 2

    while (p * p <= n): 
        #print(prime[p])
        # If prime[p] is not changed, then it is a prime 
        if (prime[p] == True): 
              
            # Update all multiples of p 
            for i in range(p * p, n+1, p): 
                prime[i] = False
        p += 1
      
    # Print all prime numbers 
    for p in range(2, n): 
        if prime[p]: 
            #print(p)
            primes.append(p)
    #print(primes)
    #print(len(primes))
    return primes


file = open("Data2.txt")
data=list(file.readlines())

for i in range(len(data)):
    data[i] = data[i].replace("\n", "")
    print(sum(findPrimes(int(data[i]))))