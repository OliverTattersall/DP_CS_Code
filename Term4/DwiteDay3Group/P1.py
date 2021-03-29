
myfile = open("DATA1.txt", "r")
data = list(myfile.readlines())

for i in range(5):
    n=len(data[i])-2

    # print(data[i], len(data[i]))
    for j in range(n+1):
        temp = data[i][0:j+1]
        # print(temp)

      

        if (n+1)%len(temp)==0:
   
            worked=True
            result=temp
            for k in range(0, n+1,len(temp)):
        #         print(k*len(temp))
                temp2 = data[i][k:(k+len(temp))]
                # if temp=="assasa":
                    # print(temp2)
                # print(temp2)
                if temp2!=temp:
                    # print(temp)
                    worked=False
                    break
            if worked:
                print(result)
                break

