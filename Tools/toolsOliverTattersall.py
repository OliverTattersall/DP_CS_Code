import random # imports module random that allows for random numbers in test cases

'''
isEven takes a single integer value a >= 0 and returns true if it is even and false otherwise
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
Given a non-empty string and an int n, return a new string where the char at index n has been removed. 
The value of n will be a valid index of a char in the original string (i.e. n will be in the range 0..len(str)-1 inclusive)

'''
def missing_char(str, n):
  front=str[:n]
  back=str[n+1:]
  return front+back
#test case
# print(missing_char('kitten', 1))




# Binary Conversion

def binCon(a):
    a=str(a)
    total=0
    place=len(a)-1
    for i in range(len(a)):
        total=total+int(a[i])*(2**(place))
        place=place-1

    return total
# test case
# print(binCon(10111111))

'''
This function takes a single positive interger parameter and returns
the sum of the digits
Paramets: i>=0
return: returns sum of the digits

precondition: i is a valid integer
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
Paramets: i>=0
return: returns sum of the digits

precondition: i is a valid integer
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

paramets: a>0, len(b)>0
return none
precondition: a is integer, b is list of integers

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

paramets: a>0, len(b)>0
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
if both strings are the same length the first string passed
will be the first substring in the new string

paramets: len(stra)>0, len(strb)>0

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

'''

def maxnum(lst):
    lst.sort()#sorts list. Affects the reference meaning original list is changed
    return lst[-1]

# testcase
# print(maxnum([2,5,7,2,1,9,20]))

'''
Function to find minimum value in a list

'''
def minnum(lst):
    lst.sort()
    return lst[0]

# testcase
# print(minnum([2,5,7,2,1,9,20]))

'''
Funtion that takes the average of the numbers in a list
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
# print(truthtable(0))


'''
Function that goes through list of strings that contain two strings separated by a space 
and splits into into two lists with the first words in the first list and the second words 
in the second list
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
Function that takes a list of integers and returns it sorted from lowest to highest

Parameters: list of Integers

Conditions 
'''
# def quickSort(lst):
#     def swap(lst, index1, index2):
#         print(lst)

#     def partition(lst, low, high):
#         print("")
#         return lst

    
#     def sort(lst, low, high):
#         if low<high:
#             p=partition(lst, low, high)

#     return sort(lst, 0, len(lst)-1)


# test case
# print(quickSort([1,9,47,20,40,52,32,4]))



'''
This function takes a list of integers and returns a sum of all integers that are multiples of 3

Parameters: list l

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
Parameters: int[] arr, int a, int b
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
Parameters: int[] values, int a, int b
Returns: int

Precondition: values is a list of integers of any size and a and b are valid positive integer values. 
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