'''
This functions finds the total possible paths created by a n*n square
Parameters: Integer n
Conditions: n>0
'''

def EulerProblem15(n):
    # creates 2-dimensional array with n+1 by n+1 dimensions, initialized with integer 1
    #Ex. if n=2, it creates: [[1,1,1], [1,1,1], [1,1,1]]
    lst=[[1 for i in range(n+1)]for i in range(n+1)] 
    for i in range(1, n+1, 1):
        for j in range(1, n+1, 1):
            lst[i][j]=lst[i-1][j]+lst[i][j-1]

    return lst[-1][-1]
            
# print(EulerProblem15(20))




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