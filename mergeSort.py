import numpy as np 
import os
import time
import math
import sys

# implementation of mergesort using divide & conqour

def combine(arr,p,q,r):
    arr1=arr[p:q+1].copy()
    arr2=arr[q+1:r+1].copy()
    count1=0
    count2=0
    sentinel=10**10
    arr1.append(sentinel)
    arr2.append(sentinel)
    for i in range(len(arr1)+len(arr2)-2):
        if arr1[count1]<=arr2[count2]:
            arr[p+i]=arr1[count1]
            count1+=1
        else:
            arr[p+i]=arr2[count2]
            count2+=1
    return arr

def MergeSort(arr,p,r):
    if r-p==1:
        if arr[p]>arr[r]:
            arr[r],arr[p]=arr[p],arr[r]
            return arr
        else:
            return arr
    elif p==r:
        return arr
    else:
        q=(p+r)//2
        arr=MergeSort(arr,p,q)
        arr=MergeSort(arr,q+1,r)
        arr=combine(arr,p,q,r)
        return arr


        

if __name__=='__main__':
    print(MergeSort([10,9,8,0,44,234,-5,1,9,11,6],0,10))  
    