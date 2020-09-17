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