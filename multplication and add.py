import numpy as np
import time
import math
import sys
import os

def addArray(arr):
    if len(arr)==1:
        return arr[0]
    else:
        return arr[0]+addArray(arr[1:])

def betterAdd(arr):
    if len(arr)==1:
        return arr[0]
    if len(arr)==2:
        return arr[0]+arr[1]
    else:
        mid = (len(arr))//2
        return betterAdd(arr[0:mid]) + betterAdd(arr[mid:])
        

def power(x,n):
    #output x^n
    if n==1:
        return x
    elif n%2==0: #even
        return power(x,n/2)*power(x,n/2)
    else:
        return power(x,(n+1)/2)*power(x,(n-1)/2)



if __name__ == "__main__":
    arr=[2,3,4,5,89,4,3,90,8,90,7,767,4,5,23,56,98,67,9]
    s=time.time()
    print(power(7,8))
    st=time.time()
    print(st-s)
