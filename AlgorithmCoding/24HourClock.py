

def findTime():
    time=input()

    if int(time[:2])>12:
        return str(int(time[:2])-12)+":"+time[3:]+" PM"

    else:
        return time+" AM"


print(findTime())