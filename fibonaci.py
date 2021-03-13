import numpy as np
import time
import math
import sys
import os

def fibo(k):
    
    if k==1:
        return 0
    if k==2:
        return 1
    else:
        return fibo(k-1)+fibo(k-2)

def betterFibo(k):
    i=1
    j=0
    while k>2:
    #    return (1,0)]
    #else:
        (i,j)=(i,j)
        p=i
        i=i+j
        j=p
        k=k-1
    return i

if __name__ == "__main__":
    #print(fibo(40))
    print(betterFibo(1000))