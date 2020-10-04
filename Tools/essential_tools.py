import random
import math

'''
This function converts a base 10 number to a base 2 number
Parameters:Integer n
Conditions: n>=0
'''
def base10ToBase2(n):

    return int(bin(n)[2:])#bin converts an integer to the string binary representation ex. bin(10)=>0b1010. the [2:] removes the 0b


# print(base10ToBase2(10))
# print(base10ToBase2(20))
# print(base10ToBase2(47))
# print(base10ToBase2(42))

'''
This Function takes a binary number and turns it into a base 10 number
Parameters: Integer a
Conditions: a contains only 1's and 0's
'''
def base2ToBase10(a):
    a=str(a)
    total=0
    place=len(a)-1
    for i in range(len(a)):
        total=total+int(a[i])*(2**(place))
        place=place-1

    return total
# test case
# print(base2ToBase10(10111111))
# print(base2ToBase10(10100))
# print(base2ToBase10(1110000))

'''
This function converts a base 2 number into a base 16 number
Parameters: String n
Conditions: n must be a valid base 2 number
'''

def base2ToHex(n):
    n=str(n) # converts n to string in case it was inputed as int
    # creates a dictionary that pairs the first sixteen binary numbers with its corresponding Hexadecimal digit
    dct={"0000":"0", "0001":"1", "0010":"2", "0011":"3","0100":"4","0101":"5","0110": "6","0111":"7", "1000":"8", "1001":"9", "1010": "A", "1011":"B","1100":"C","1101":"D","1110":"E", "1111":"F"}
    
    result=""
    if len(n)%4!=0:
        n=(4-(len(n)%4))*"0"+n
    while len(n)!=0:
        result+=dct[n[-4:]]#gets the last 4 digits of n and searchs through the dictionary for the corresponding key, adding the Hex value to the string
        n=n[0:-4]
    return result[::-1]#returns reversed result as each item is appended not put at the beginning

# print(base2ToHex("1001010101010"))
# print(base2ToHex(10010100101))

'''
This function converts a base 2 number into a base 16 number
Parameters: String n
Conditions: n must be a valid base 2 number
'''
def base2ToHexB(n):
    #hex converts a decimal value into its corresponding hexadecimal string
    return hex(base2ToBase10(n))[2:]
# print(base2ToHexB("1001010101010"))
# print(base2ToHexB(10010100101))

'''
This function converts a Hex value into a base 2 value
Parameters: String n
Conditions: n must be a valid Hex value
'''

def HexToBase2(n):
    n=str(n)
    #dictionary of hexadecimal with its corresponding binary value
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
# print(HexToBase2("FF"))
# print(HexToBase2(70))
#print(HexToBase2("4A5"))

'''
This function converts a Hex value into a base 2 value using built in bin function
Parameters: String n
Conditions: n must be a valid Hex value
'''
def HexToBase2B(n):
    return int(str(bin(int(n,16)))[2:])

# print(HexToBase2B("12AA"))
# print(HexToBase2("FF"))
# print(HexToBase2(70))
#print(HexToBase2("4A5"))

'''
This function takes a single positive interger parameter and returns
the sum of the digits
Parameters: Integer i
return: returns sum of the digits
precondition: i>=0
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
#print(sumDigits("892"))
# print(sumDigits(0))

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
# print(findModSum1([1,6,9,1,-3,12,3,8]))
# print(findModSum1([random.randint(1,100) for i in range(20)]))

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
# print(findModSum2([random.randint(1,100) for i in range(20)], random.randint(1,50), random.randint(25,75)))

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
# print(findModSum3([random.randint(1,100) for i in range(20)], random.randint(1,10), random.randint(1,10)))

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
# print(reverseWordA("hello goodbye"))
# print(reverseWordA("ks!&#^)!#&$&"))

'''
 The function takes a list of Strings and returns a new string of each word constructed in reverse.  

Parameters: String a
Returns: String

Precondition:  a list of any length and it contains strings of any length
'''

def reverseWordB(lst):
    result=''
    for i in range(len(lst)):
        result+=lst[i][::-1]

    return result

# testcase
# print(reverseWordB(['cat', 'dog']))
# print(reverseWordB(["hello", "goodbye", "ciao", "123*(!@&#*)$"]))