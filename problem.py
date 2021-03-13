import numpy as np
import time
import math
import sys
import os

# to solve find the min element in a r times circular sorted array

def FindMin(arr):
    if len(arr)==2 and arr[0]>arr[1]:
        return arr[1]
    else:
        if arr[0]>arr[len(arr)//2]:
            return FindMin(arr[0:len(arr)//2+1])
        elif arr[len(arr)//2]>arr[-1]:
            return FindMin(arr[len(arr)//2:])
        else:
            return arr[0]

if __name__ == "__main__":
    arr=np.arange(0,100000)
    arr=list(np.roll(arr,-1))
    start=time.time()
    FindMin(arr)
    stop=time.time()
    print(stop-start)


