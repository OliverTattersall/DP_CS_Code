
'''
This Function takes two lists of strings and add strings in the same index together in any order.
If one list is longer than the other the none paired indexes should be included in c.
Parameters: String[] a, String[] b
PostConditions: The two passed lists remain unchanged
return String[]
'''

def mergeStrings(a,b):
    #creates a copy of list 'a' so that result is not just a reference to the same list but the same content in a new list and 
    # changeable without breaking postcondition
    result=a.copy()

    #loops through b
    for i in range(len(b)):
        #if the index is not in result, it adds the extra values
        if i>len(result)-1:
            result.append(b[i])
        #if the index is in result it concatenate the existing string and the string in b
        else:
            result[i]=result[i]+b[i]

    
    return result

# print(mergeStrings(['cat','dog',"fish"],["one"]))
# print(mergeStrings([],["one","two","three"]))
# print(mergeStrings(['red','green'],['six','seven']))

# lst1=['cat','dog',"fish"]
# lst2=['six','seven']
# print(mergeStrings(lst1 ,lst2))
# print(lst1) #unchanged
# print(lst2) #unchanged

'''
This functions searches through a list for the first instance of a value target. If it is not in the list it returns "not in list"
Parameters: List[] lst, Integer/String target
Returns index or "not in list"
'''

def linearSearch(lst, target):
    #a for loop that loops through every value in lst
    for i in range(len(lst)):
        #tests to see if the lst[i] = the target value if so it returns the index
        if lst[i]==target:
            return i

    #this return only occurs if the return inside the for loop is never called as the target value is not in the list
    return "not in list"

# print(linearSearch([1,3,8,12,43, 320, 10, 203,11], 10))
# print(linearSearch([1,3,8,12,43, 320, 10, 203,11], 40))
# print(linearSearch([], 10))
# print(linearSearch(['1','3','8','12','43',' 320',' 10',' 203','11'], 10))
# print(linearSearch(['1','3','8','12','43','320','10','203','11'], '10'))
# print(linearSearch([1.2,3.2,"8",1.2,0.43, 3.20, 1.0, '203',11], 1.0))

'''
This function creates a dictionary of perfect squares between 1 and n inclusive. The keys for this value are the squareroots, Ex. 2:4 would be one pair.
Parameters: Integer n
Condtions: n>1

'''
def dictFun(n):
    n=int(n)
    #creates a dictionary with the key x, and the value x*x for x values between 1 and n inclusive
    dct={x:x*x for x in range(1,n+1,1)}
    return dct

# print(dictFun(10)) 
# print(dictFun(1))
# print(dictFun('4'))