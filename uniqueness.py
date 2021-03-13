import numpy as np
import time
import math
import sys
import os
#check for uniqness using recursiion
def unique(arr):
     
    if len(arr)==1:
        return True
    else:
        if not unique(arr[1:]):
            return False
        if not unique(arr[0:len(arr)-1]):
            return False
        else:
            return arr[0]!=arr[-1]
        
if __name__ == "__main__":
    arr=[2, 4, 5, 7, 8, 9, 12, 14, 17, 19, 12, 25, 27,28, 33, 37]
    print(unique(arr))
                   