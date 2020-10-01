import random # imports module random that allows for random numbers in test cases
import math # imports math module which contains math functions such as math.sqrt(n) which finds the square root of n
'''
isEven takes a single integer value a >= 0 and returns true if it is even and false otherwise
Parameters: Integer a
Conditions: 0<=a<10
'''


def isEven(a):
    if a%2==0:
        return True

    else:
        return False

#test code
# print(isEven(3))
# print(isEven(6))
# print(isEven(2))

'''
This functions takes an integer and returns if all digits in it are Even
Parameters: Integer n
Conditions: n>0
'''
def allEven(n):
    even=True
    while(n>0)and(even==True):
        if(n%10)%2==1:
            even=False
        n=n//10
    return even

# testcode
# print(allEven(256))
# print(allEven(246))

'''
Given a non-empty string and an int n, return a new string where the char at index n has been removed. 
Parameters: String a
Conditions: 0<n<len(a)-1
'''
def missing_char(a, n):
  front=a[:n]
  back=a[n+1:]
  return front+back
#test case
# print(missing_char('kitten', 1))


'''
This function takes a single positive interger parameter and returns
the sum of the digits
Parameters: Integer i
return: returns sum of the digits

precondition: i>0
'''

def sumDigits(a):
    sumdigits=0
    #casting is the process of changing type
    a=str(a)

    #Fundamental skill: looping through string

    #count, check, change
    for i in range(0, len(a), 1):
        sumdigits+=int(a[i])

    return sumdigits
#test case
#print(sumDigits(123))


'''
This function takes a single positive interger parameter and returns
the sum of the digits
Parameters: Integer i
return: returns sum of the digits

precondition: i>=0
'''
def sumDigitsA(a):
    total=0

    while(a>0):
        total+=a%10 # access the ones digit
        a=a//10 # integer division that removes ones digit

    # Trace
    # a=57

    # a| a>0
    # 57| 57>0| TRUE RUN LOOP tptal = 0 +7, a=5
    # 5| 5>0| TRUE RUN LOOP total=7+5, a=0
    # 0|0>0| FALSE EXIT LOOP

    return total
#test case
#print(sumDigitsA(1234))

'''
This function takes an integer, a,  and a list of integers, b, and scales
each integer in the list by a, the first integer. 

parameters: Integer a, List b
return none


'''
def scaleElementsA(a, b):
    
    for i in range(len(b)):
        b[i]=b[i]*a

    #return b

# test case
# l=[1,2,3,4]
# scaleElementsA(2, l)
# print(l)


'''
This function takes an integer, a,  and a list of integers, b, and scales
each integer in the list by a, the first integer. 

parameters: a>0, len(b)>0
return b
precondition: a is integer, b is list of integers
'''

def scaleElementsB(num, list):
    newlst=[]
    for i in range(len(list)):
        newlst.append(list[i]*num)
    return newlst

#test case
#print(scaleElementsB(2, [1,2,3,4]))

'''
This function takes an integer, a,  and a list of integers, b, and scales
each integer in the list by a, the first integer. 

paramets: a>0, len(b)>0
return b
precondition: a is integer, b is list of integers

'''
import numpy #import numpy library which is a library full of support for large, multi-dimensional arrays 
             #and matrices, along with a large collection of high-level mathematical functions 
def scaleElementsC(a, b):
    b=numpy.array(b) #casts the lst of intergers into a numpy array that allowed math functions applied to the whole array at once
    return list(b*a) # multiples each item in the list b by a and casts the array back to a list then returns it

#test case
#print(scaleElementsC(2, [1,2,3,4]))


'''
this function takes two strings, stra and strb, and returns a new string
in the form of Larger string+Smaller string

parameters: String stra, String strb
Conditions: len(stra)>0, len(strb)>0

'''

def addStringsSmallLarge(stra, strb):
    str=""
    if len(stra)>=len(strb):
        str=stra+strb
    else:
        str=strb+stra
    return str

# test case
# print(addStringsSmallLarge("banana", "mango"))


'''
Function to find maximum value in a list
Parameters: List lst
Conditions: len(lst)>0

'''

def maxnum(lst):
    lst.sort()#sorts list. Affects the reference meaning original list is changed
    return lst[-1]

# testcase
# print(maxnum([2,5,7,2,1,9,20]))

'''
Function to find minimum value in a list
Parameters: List lst
Conditions: len(lst)>0
'''
def minnum(lst):
    lst.sort()
    return lst[0]

# testcase
# print(minnum([2,5,7,2,1,9,20]))

'''
Funtion that takes the average of the numbers in a list
Parameters: List lst
Conditions: len(lst)>0
'''

def average(lst):
    return int(sum(lst)/len(lst))

# print(average([1,2,3]))

'''
Function that creates a truth table that will have n columns.
Returns a string containing n columns with 2^n lines, each line contains 1 combination

Parameters: Integer n

Preconditions: n>=0
'''

def truthtable(n):
    table=[]
    table2=[]
    temp=[]
    total=2**n
    finalstr=""
    for i in range(n):
        on=False
        count=2**(i)
        timer=count
        for j in range(total):
            if timer==0:
                if on:
                    on=False
                else:
                    on=True
                timer=count
            if on:
                temp.append(1)
            else:
                temp.append(0)
            timer=timer-1
        table.insert(0, temp)
        temp=[]

    for i in range(total):
        temp=[]
        for j in range(len(table)):
            temp.append(table[j][i])
            finalstr+=str(table[j][i])
            if j==n-1:
                finalstr+="\n"
        table2.append(temp)
        
    print(table2)
    return finalstr

# testcase
# print(truthtable(4))


'''
Function that goes through list of strings that contain two strings separated by a space 
and splits into into two lists with the first words in the first list and the second words 
in the second list
Parameters: List lst
Conditions: len(lst)>0
'''

def splitthestr(lst):
    first=[]
    second=[]
    for i in range(len(lst)):
        a,b=lst[i].split(" ")
        first.append(a)
        second.append(b)

    return first, second

# test case
# print(splitthestr(["hello world", "good bye", "good morning"]))



'''
This function reads the content of the file and copy it to a list.  It returns the list containing the files contents.

Parameter: String name

Precondition - name is a valid file name
'''

def readFileToList(str):
    myfile=open(str, "r")
    lst=myfile.readlines()
    return lst

# print(readFileToList("test"))

'''
This function takes the passed list and copy the contents into the file named name. 

Parameter: List l, String name

Returns: a list containing all the elements in the file name
'''

def writeListToFile(lst, str):
    myfile=open("..//"+str, "a")
    for i in range(len(lst)):
        myfile.write(lst[i]+"\n")

    myfile.close()
# writeListToFile(["hello", "mr", 'johnson'], "test")


'''
Function takes integer n and finds all primes between 0 and n inclusive

Parameters: Integer n

Conditions: n>2
'''

def findPrimes(n):
    
    primes=[] #list where all primes will go into
    prime=[True for i in range(n+1)] #list intiated with n+1 True values
    p=2 # initial number to search through as all multiples of 0 and 1 are 0 and 1 and will never increase

    while p*p<=n: #loops from 2 to √n as the highest possible factor that would not be 
                  #eliminated would be √n. Ex. 36, any factors higher than 6 would have been eliminated already: 18 by 2, 12 by 3
        if prime[p]==True: #tests if the current p value is a prime so it can eliminate all multiples
            
            for i in range(p*p, n+1, p): # loops from 
                prime[i]=False

        p+=1 # increments p to test the next integer

    for i in range(2, n+1, 1): # loops from 2 to n
        if prime[i]==True: # tests to see if that number is prime
            primes.append(i) # if prime appends it to the list primes

    return primes #returns list of primes between 2 and n inclusive
# testcase
# print(findPrimes(13))




'''
This function takes a list of integers and returns a sum of all integers that are multiples of 3
Parameters: List l
Preconditions: list must have integers
'''

def findModSum1(lst):
    sum=0
    for i in range(len(lst)):
        if lst[i]%3==0:
            sum=sum+lst[i]
    return sum

# testcase
# print(findModSum1([1,6,9,1,5,9,0,3]))

'''
This function takes a list of integers and returns a sum of all integers that are between a and b
Parameters: List lst, Integer a, Integer b
Returns: int

'''
def findModSum2(lst, a, b):
    sum=0
    if a>b:
        temp=b
        temp2=a
        a=temp
        b=temp2
    for i in range(len(lst)):
        if lst[i]>a and lst[i]<b:
            sum=sum+lst[i]

    return sum

# testcase
# print(findModSum2([1,2,3,4,5,6,7], 6, 2))

'''
This function takes a list of integers and two integers and returns the sum of all integers that are not factors of a or b

Name: findModSum3
Parameters: List values, int a, int b
Returns: int

Precondition: a>0, b>0
'''
def findModSum3(lst, a, b):
    sum=0
    for i in range(len(lst)):
        if lst[i]%a==0 and lst[i]%b==0:
            
            sum=sum+lst[i]

    return sum

# testcase
# print(findModSum3([1,2,3,4,5,6,7], 3, 2))


'''
This Function takes a list of floats and returns the sum of all digits
Parameters: List lst

'''

def findModSum4(lst):
    sum=0
    string=''
    for i in range(len(lst)):
        string+=str(lst[i])
    string=string.replace(".", "")
    for i in range(len(string)):
        sum+=int(string[i])
    return sum

# testcase
# print(findModSum4([1.2, 3.14, 7.89]))

'''
The function takes a Strings and returns the string in reverse 

Name: reverseWordA
Parameters: String a
Returns: string

'''
def reverseWordA(a):
    return a[::-1]

# testcase
# print(reverseWordA("cat"))

'''
 The function takes a list of Strings and returns a new string of each word constructed in reverse.  

Name: reverseWordB
Parameters: String[] a
Returns: String

Precondition: a list a list of any length and it contains strings of any length
'''

def reverseWordB(lst):
    result=''
    for i in range(len(lst)):
        result+=lst[i][::-1]

    return result

# testcase
# print(reverseWordB(['cat', 'dog']))


'''
Function finds sum of all even fibonacci numbers between 0 and n

parameters: Integer n

Conditions n>0
'''

def EulerProblem2(n):
    fib=[1,1] 
    sum=0
    while fib[-1]<n:
        newval=fib[-1]+fib[-2]
        if newval%2==0:
            sum+=newval
        fib.append(newval)
    return sum

# test case
# print(EulerProblem2(4000000))

'''
This function finds the largest prime factor in the number n
Parameters: Integer n
Conditions: n>0
'''

def EulerProblem3(n):
    primelst=findPrimes(n) #find primes between 2 and n using a findPrimes() function above.  
    unfound=False
    count=len(primelst)-1
    largest=0
    while unfound!=True:
        if n%primelst[count]==0:
            largest=primelst[count]
            unfound=True
        count=count-1

    return largest

# print(EulerProblem3(600851475143))
# print(EulerProblem3(19))

'''
This Function finds the largest palindrome that is the product of 2 n-digit factors. 
Parameter: Integer n
Conditions: n>0
'''

def EulerProblem4(n):
    highestproduct=int("9"*n)**2
    print(highestproduct)
    for i in range(highestproduct, 0, -1):
        if str(i)==str(i)[::-1]:
            # print(i)
            for j in range(i,10**(n-1), -1):
                if i%j==0:
                    if len(str(j))==n and len(str(i//j))==n:
                        return j*(i//j)
            
# print(EulerProblem4(2))
# print(EulerProblem4(3))


'''
This function finds the difference between ((1+2..+n)^2)-(1^2+2^2...+n^2)
Parameters: Integer n
Conditions: n>0
'''
def EulerProblem6(n):
    sum1=0
    sum2=sum([i for i in range(1, n+1)])**2
    for i in range(1, n+1):
        sum1+=i**2
    return sum2-sum1

# print(EulerProblem6(100))

'''
This function finds the nth prime
Parameters: Integer n
Conditions: n>0
'''

def EulerProblem7(n):
    test=False
    counter=n*10
    while test!=True:
        lst=findPrimes(counter)
        if len(lst)>=n:
            test=True
            return lst[n-1]
        counter=counter*5

# print(EulerProblem7(10001))

'''
This function takes integer n and t and returns the highest product formed by t consecutive digits in n
Parameters: Integer n, Integer t
Conditions: n>0, 0<t<n
'''

def EulerProblem8(n, t):
    product=0
    n=str(n)
    possibilities=[]
    
    #this while removes the digits not available because they would have a 0 in their product
    while n.count("0")!=0:
        # print(len(n)) # all print functions inside this function are used as testing methods to see the process
        index=n.find("0")
        # print(index)
        ind=n.find("0", index+1)
        # print(ind)
        if index<=t:
            
            # ind=n.find("0", index+1)
            if ind-index<=13 and ind!=-1:
                # print(True)
                # print(n[0:ind])
                n=n[ind:]
            else:
                n=n[index+1:]
        elif index>t and ind!=-1:
            possibilities.append(n[0:index])
            # ind=n.find("0", index+1)
            if ind-index<=13:
                n=n[ind-1:]
            else:
                n=n[index+1:]
            
        elif index<=t and ind==-1:
            if len(n)-index<=t:
                n=""
            else:
                n=n[index+1:]
            
        elif index>t and ind==-1:
            possibilities.append(n[0:index])
            if len(n)-index<=t:
                n=n[0:index]
            else:
                possibilities.append(n[index+1:])
                n=""
    

    print(possibilities)#list full of groups of numbers that can be searched through 

    #for loop that looks through each item in possibilities 
    for h in range(len(possibilities)):
        
        #for loop that goes through every consequitive 13 digits in possibilities[h]
        for i in range(len(possibilities[h])-t+1):
            temp=possibilities[h][i:i+t]

            temp2=1
            #for loop that goes through every digit and multiplies it to a temp value to get the product of the 13 digits
            for j in range(len(temp)):
                temp2=temp2*int(temp[j])
                # print(temp2)
            if temp2>product:
                    product=temp2

    return product


# print(EulerProblem8(7316717653133062491922511967442657474235534919493496983520312774506326239578318016984801869478851843858615607891129494954595017379583319528532088055111254069874715852386305071569329096329522744304355766896648950445244523161731856403098711121722383113622298934233803081353362766142828064444866452387493035890729629049156044077239071381051585930796086670172427121883998797908792274921901699720888093776657273330010533678812202354218097512545405947522435258490771167055601360483958644670632441572215539753697817977846174064955149290862569321978468622482839722413756570560574902614079729686524145351004748216637048440319989000889524345065854122758866688116427171479924442928230863465674813919123162824586178664583591245665294765456828489128831426076900422421902267105562632111110937054421750694165896040807198403850962455444362981230987879927244284909188845801561660979191338754992005240636899125607176060588611646710940507754100225698315520005593572972571636269561882670428252483600823257530420752963450,13))



'''
This function finds the sum of the primes between 0 and n
Parameters: Integer n
Conditions: n>2 
'''

def EulerProblem10(n):
    primelst=findPrimes(n)
    return sum(primelst)

# print(EulerProblem10(2000000))

'''

'''

def EulerProblem11(lst, n):
    product=0
    for i in range(len(lst)-n+1):
        for j in range(len(lst[i])-n+1):
            temp=[]
            temp.append(int(lst[i][j])*int(lst[i][j+1])*int(lst[i][j+2])*int(lst[i][j+3]))
            temp.append(int(lst[i][j])*int(lst[i+1][j])*int(lst[i+2][j])*int(lst[i+3][j]))
            temp.append(int(lst[i][j])*int(lst[i+1][j+1])*int(lst[i+2][j+2])*int(lst[i+3][j+3]))
            # if i==16 and j==16:
            #     # print(temp[2])
            temp.sort()
            if temp[2]>product:
                product=temp[2]
    for i in range(len(lst)-1, len(lst)-n+1, -1):
        for j in range(len(lst[i])-n+1):
            temp2=1
            temp3=1
            temp2=int(lst[i][j])*int(lst[i][j+1])*int(lst[i][j+2])*int(lst[i][j+3])
            temp3=int(lst[j][i])*int(lst[j+1][i])*int(lst[j+2][i])*int(lst[j+3][i])
            # if i==19 and j==16:
            #     print(temp2)
            #     print(temp3)

            if temp2>product:
                product=temp2
            if temp3>product:
                product=temp3
    
    for i in range(n-1, len(lst), 1):
        for j in range(len(lst[i])-n+1):
            temp4=1
            temp4=int(lst[i][j])*int(lst[i-1][j+1])*int(lst[i-3][j+3])*int(lst[i-3][j+3])
            if temp4>product:
                product=temp4


    return product

#test case
#current answer: 66845319, incorrect
# total=[]
# for i in range(20):
#     total.append(input().split(" "))

# print(EulerProblem11(total, 4))

'''
This Function finds all factors of positive integer n
Parameters: Integer n
Conditions: n>1
'''

def findFactors(n):
    factors=set([]) #creates a set named factors. when adding an item to a set, if it is already in there, it will not add a duplicate
    #loop from 1 to √n+1 as √n is the highest factor possible, taking the lower factor of a pair. ex. 36: (1,36),(2,18),(3,12),(4,9),(6,6) 6 is the highest factor out of the lower factor in a pair and 6 is the √36
    for i in range(1,int( math.sqrt(n))+1, 1):
        if n%i==0:
            factors.add(i)
            factors.add((n//i))

    factors=list(factors)
    factors.sort()
    return factors

# print(findFactors(25))

'''
This Function finds the first triangle number with more than 500 factors
Paramters: Integer n
Conditions: n>0
'''

def EulerProblem12(n):
    test=False
    triangles=[1]
    while test==False:
        if len(findFactors(triangles[-1]))>n:
            test=True
            return triangles[-1]
        else:
            triangles.append((len(triangles)+1)**2-triangles[len(triangles)-1])


# print(EulerProblem12(500))

'''
This functions finds the total possible paths created by a n*n square
Parameters: Integer n
Conditions: n>0
'''
#
#Might use this one for simple
#
def EulerProblem15(n):
    lst=[[1 for i in range(n+1)]for i in range(n+1)] # creates 2-dimensional array with n+1 by n+1 dimensions, initialized with integer 1
    for i in range(1, n+1, 1):
        for j in range(1, n+1, 1):
            lst[i][j]=lst[i-1][j]+lst[i][j-1]

    return lst[-1][-1]
            
# print(EulerProblem15(20))

'''

'''

def EulerProblem16(n):
    num=2**n
    num=str(num)
    sum=0
    for i in range(len(num)):
        sum=sum+int(num[i])

    return sum
# print(EulerProblem16(1000))

'''
This function finds the sum of all letters in the number from 1 to n inclusive.
Parameters: Integer n
Condition: 0<n<1000
'''

def EulerProblem17(n):
    # dict with numbers and how many characters that number has
    dct={1:3, 2:3, 3:5, 4:4, 5:4,6:3,7:5, 8:5, 9:4, 10:3, 11:6, 12:6, 13:8, 14:8, 15:7, 16:7, 17:9, 18:8, 19:8, 20:6, 30:6, 40: 5, 50: 5, 60: 5, 70:7, 80:6, 90: 6, 100:7}
    totalletters=0
    for i in range(1, n+1, 1):
        temp=[]
        for j in range(len(str(i))-1, -1, -1):
            if int(str(i)[-2:])>10 and int(str(i)[-2:])<20:
                temp.append(int(str(i)[-2:]))
                if i>100:
                    temp.insert(0, i-int(str(i)[-2:])) 
                break
            temp.insert(0, int(str(i)[j])*(10**(len(str(i))-1-j)))
        temp3=0
        for j in range(len(temp)):
            if temp[j]!=0:
                if temp[j]>=100 and i%100!=0:
                    # print(temp[j]//100)
                    totalletters+=dct[100]+dct[temp[j]//100] + 3
                    temp3+=dct[100]+dct[temp[j]//100] + 3
                elif i%100==0:
                    totalletters+=dct[100]+dct[temp[j]//100] 
                    temp3+=dct[100]+dct[temp[j]//100] 
                else:
                    totalletters+=dct[temp[j]]
                    temp3+=dct[temp[j]]

    return totalletters

# print(EulerProblem17(999))
# print(EulerProblem17(1))

'''
This function converts a base 2 number into a base 16 number
Parameters: String n
Conditions: n must be a valid base 2 number
'''

def base2ToHex(n):
    n=str(n)
    print(n[-4:])
    dct={"0000":"0", "0001":"1", "0010":"2", "0011":"3","0100":"4","0101":"5","0110": "6","0111":"7", "1000":"8", "1001":"9", "1010": "A", "1011":"B","1100":"C","1101":"D","1110":"E", "1111":"F"}
    result=""
    print(len(n))
    if len(n)%4!=0:
        n=(4-(len(n)%4))*"0"+n
    while len(n)!=0:
        result+=dct[n[-4:]]
        n=n[0:-4]
    return result[::-1]

# print(base2ToHex("1001010101010"))

'''
This function converts a Hex value into a base 2 value
Parameters: String n
Conditions: n must be a valid Hex value
'''

def HexToBase2(n):
    n=str(n)
    dct={'0': '0000', '1': '0001', '2': '0010', '3': '0011', '4': '0100', '5': '0101', '6': '0110', '7': '0111', '8': '1000', '9': '1001', 'A': '1010', 'B': '1011', 'C': '1100', 'D': '1101', 'E': '1110', 'F': '1111'}
    result=""
    for i in range(len(n)):
        result+=dct[n[i]]
    test=True
    while test!=False:
        if result[0]!="1":
            result=result[1:]
        else:
            test=False
    return result
# print(HexToBase2("12AA"))

'''
This function finds the sum of the digits of n!
Parameters: Integer n
Condition: n>0
'''
def EulerProblem20(n):
    num=1
    for i in range(1, n+1,1):
        num=num*i
    num=str(num)
    sum=0
    for i in range(len(num)):
        sum+=int(num[i])
    return sum

# print(EulerProblem20(100))

