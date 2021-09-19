import time
import random
# import sys
# sys.setrecursionlimit(1500)


lst=[random.randint(1,1000) for i in range(10)]
# lst=[i for i in range(100)][::-1]
# lst=[10, 80, 30, 90, 40, 50, 70]

def partition(arr, lo, hi):
    p = arr[(hi+lo)//2]
    i=lo-1
    j=hi+1
    while True:
        i+=1
        while arr[i]<p:
            i+=1
        j-=1    
        while arr[j]>p:
            j-=1

        if i>=j:
            return j
        arr[i], arr[j] = arr[j],arr[i]


def quicksort(arr, lo,hi):
    if lo<hi:
        p=partition(arr, lo, hi)
        quicksort(arr, lo, p)
        quicksort(arr, p+1, hi)

if __name__=="__main__":
    start_time1 = time.time()
    quicksort(lst,0, len(lst)-1)

    #print(lst2)

    print("--- %s seconds ---" % (time.time() - start_time1))
    print(lst)