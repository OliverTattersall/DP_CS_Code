'''
This functions finds the total possible paths created by a n*n square
Parameters: Integer n
Conditions: n>0
'''

def EulerProblem15(n):
    # creates 2-dimensional array with n+1 by n+1 dimensions, initialized with integer 1
    #Ex. if n=2, it creates: [[1,1,1], [1,1,1], [1,1,1]]
    #this is meant to represent a square, with each item in lst being a row 
    lst=[[1 for i in range(n+1)]for i in range(n+1)] 

    # loops from the second row until the last row, with i being the index of each row
    # it skips the first row because the first row and first column need to be kept as ones 
    for i in range(1, n+1, 1):
        #Loops from the second column until the last column in each row
        for j in range(1, n+1, 1):
            #lst[i][j] becomes the number from the row before in the same column added to the number in
            lst[i][j]=lst[i-1][j]+lst[i][j-1]

    # Trace, n=2
    # lst=[[1,1,1], [1,1,1], [1,1,1]]
    # i | j | lst[i-1][j] | lst[i][j-1] | lst[i][j]
    # 1 | 1 | 1           | 1           | 2 
    # 1 | 2 | 1           | 2           | 3
    # 2 | 1 | 2           | 1           | 3 
    # 2 | 2 | 3           | 3           | 6
    # Output= 6  

    #returns the last number in the last row of lst which will be the highest number with all the combinations
    return lst[-1][-1]
            
# print(EulerProblem15(20))
# print(EulerProblem15(1))
# print(EulerProblem15(2))
# print(EulerProblem15(3))
# print(EulerProblem15(5))
# for i in range(1,21):
#     print(EulerProblem15(i))




'''
This function finds the sum of all letters in the number from 1 to n inclusive.
Parameters: Integer n
Condition: 0<n<1000
'''

def EulerProblem17(n):
    # dictionary with numbers and how many characters that number has
    # ex. one has 3 letters therefore the key one is paired with the item 3, 1:3

    # A dictionary is a data structure that is unordered and changeable. Each item is paired with a key.  
    # Using that key is how each item is accessed. Unlike with lists, Items cannot be obtained by index 
    # meaning the first item cannot be obtained by doing dct[0] like in a lst but it can only be obtained by dct[key]
    dct={1:3, 2:3, 3:5, 4:4, 5:4,6:3,7:5, 8:5, 9:4, 10:3, 11:6, 12:6, 13:8, 14:8, 15:7, 16:7, 17:9, 18:8, 19:8, 20:6, 30:6, 40: 5, 50: 5, 60: 5, 70:7, 80:6, 90: 6, 100:7}
    
    #this is an ongoing sum of the total letters
    totalletters=0

    #Loops from 1 to n+1 inclusive. This loop will go through every number and find its length
    for i in range(1, n+1, 1):
        #temporary list that will get wiped for every number. It will contain each digit broken up into parts. 
        # Ex. 324 will become [300,20,4] in the temp list
        temp=[]

        #loops from the last digit of i to the first inclusive
        for j in range(len(str(i))-1, -1, -1):
            # tests if the number is between 10 and 20 exclusive as 11-19 follow different patterns than other 2 digit numbers
            # for example twenty nine can be broken up into 20 and 9 to find the letters but nineteen cannot be broken up into 
            # ten and nine, the letter count is different
            if int(str(i)[-2:])>10 and int(str(i)[-2:])<20:
                #Appends the last two digits of the number to the temporary list
                temp.append(int(str(i)[-2:]))
                #tests if the number is greater than one hundred
                #if it is it adds i - the last two digits to add a number divisble by 100. 
                #Ex. 119, adds 19 right above then adds 119-199, 100, now the temporary array has 100,19
                if i>100:
                    temp.insert(0, i-int(str(i)[-2:])) 
                #breaks the for loop meaning j will not continue to decrement until it reaches -1, it will just stop. 
                # This does not break the outer loop that loops i only the loop that loops j
                break
            #if the last 2 digits are not in the teens, this loop takes each digit and multiplies it by its corresponding value and adds it to the temporary list at the beginning of the list using insert method
            # the ones column is multiplied by one, or 10^0, the tens column is multiplied by 10, or 10^-1, and the hundreds column is multiplied by 100, or 10^2
            temp.insert(0, int(str(i)[j])*(10**(len(str(i))-1-j)))
            # Trace Table, i=324
            # j | str(i)[j] | len(str(i))-1-j | 10**len(str(i))-1-j | temp
            # 
            # 2 | 4         | 0               | 1                   | [4|
            # 1 | 2         | 1               | 10                  | [20,4|
            # 0 | 3         | 2               | 100                 | [300, 20,4|


        #loops through the temporary list containing the parts of the number
        for j in range(len(temp)):
            #makes sure to see if the number isn't 0 as 0 can be added through numbers like 30 but the letters of zero don't add to the total letters of 30 as it is not thirty zero its just thirty
            if temp[j]!=0:
                #tests to see if the number is greater or equal 100 and if i is divisible by 100 as the hundreds have to be broken up further
                #Ex. i=201, temp[j]=200, splits into 2 and 100 as the word is two hundred
                if temp[j]>=100 and i%100!=0:
                    #adds the letters of 100 and of the multiplier, 2 in the above case, as well as 3 for the three letters in 'and'
                    # adds the letters by using the number as a key in the dictionary and getting its corresponding value
                    totalletters+=dct[100]+dct[temp[j]//100] + 3
                    # the // simple is for integer division meaning the return will be an integer, ex. 200/100 =2.0, 200//100=2
                #tests to see if i is divisible by a hundred as it will not need to add the 3 extra letters for and
                # Ex. 100= one hundred, no and
                elif i%100==0:
                    totalletters+=dct[100]+dct[temp[j]//100] 

                #if it is not greater than 100 than that number is used as a key and the value is added to total letters
                else:
                    totalletters+=dct[temp[j]]

    #returns an integer stating the total letters between 1 and n
    return totalletters

# print(EulerProblem17(999))
# print(EulerProblem17(1))
# print(EulerProblem17(5))