first=input()
second=input()

def compare(first, second):
    firstletters={}
    secondletters={}

    for i in range(len(first)):

        firstletters[first[i]]=firstletters.get(first[i], 0)+1
        secondletters[second[i]]= secondletters.get(second[i], 0)+1
    
    if firstletters==secondletters:
        return "A"

    letters=list(firstletters.keys())
    # print(letters)
    count=0
    for i in range(len(letters)):
        if letters[i] in secondletters:
            if firstletters[letters[i]]>=secondletters[letters[i]]:

                firstletters[letters[i]]=firstletters[letters[i]]-secondletters[letters[i]]
                del secondletters[letters[i]]
                # count += firstletters[letters[i]]

            else:
                return 'N'
                # secondletters[letters[i]] = secondletters[letters[i]]-firstletters[letters[i]]
                # del firstletters[letters[i]] 

        count+=firstletters[letters[i]]

            



    # print(firstletters, secondletters, count)


    if count == secondletters.get("*", 0):
        return "A"

    else:
        return "N"

print(compare(first, second))