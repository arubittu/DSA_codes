import numpy as np
import time
import math
import sys
import os

# problem of drawing ruler thru recursion

def ruler(ticks):
    if ticks==1:
        pass
    else:
        ruler(ticks-1)
        print('_'*(ticks-1))
        ruler(ticks-1)
    
if __name__ == "__main__":
    inches=int(input('enter inches:'))
    ticks=int(input('enter ticks:'))

    for i in range(0,inches+1):
        
        print('{} {}'.format(i,'_'*ticks))
        if i==inches:
            break
        ruler(ticks)
    
