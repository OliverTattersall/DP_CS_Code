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

# print(binCon(10111111))