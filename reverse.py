import numpy as np
import time
import math
import sys
import os

# reverse array of numbers using recursion and rec with parameterization.
def reverse(arr):
    
    if len(arr)==1:
        q=arr
        return q
    else:
        q=arr[1:]
        b=reverse(q) 
        b.append(arr[0])
        return b

def areverse(arr,start,stop):
    if stop-start<=1:
        return arr
    else:
        arr[start],arr[stop]=arr[stop],arr[start]
        return areverse(arr,start+1,stop-1)
    

if __name__ == "__main__":
    arr=[2, 4, 5, 7, 8, 9, 12, 14, 17, 19, 22, 25, 27,28, 33, 37]
    print(reverse(arr))
    print(areverse(arr,0,len(arr)-1))