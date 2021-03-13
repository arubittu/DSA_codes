import numpy as np
import time
import math
import sys
import os

#binary search using recurion, given a sorted array
def BinarySearch(arr,target,min,max):
    #arr=arr[min:max+1]
    if min>max:
        return False
    if arr[(max+min)//2]==target:
        return (max+min)//2 
    elif target <arr[(max+min)//2]:
       
        return BinarySearch(arr,target,min,(max+min)//2-1)
    elif target >arr[(max+min)//2]:
        return BinarySearch(arr,target,(max+min)//2+1,max)


    
if __name__ == "__main__":
     arr=[2, 4, 5, 7, 8, 9, 12, 14, 17, 19, 22, 25, 27,28, 33, 37]
     print(BinarySearch(arr,28,0,len(arr)-1))
