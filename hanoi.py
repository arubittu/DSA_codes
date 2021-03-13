import numpy as np
import sys
import os
import time

# tower of hanoi problem using recursion

def hanoi(n): #remember to generalize for all n using range fucntion
    pole_dict={'A':[*range(1,n+1,1)],'B':[],'C':[]}  #initialize
    one_state='A'
    while pole_dict['B']!=[*range(1,n+1,1)]:
        #perform 1st step
        if n%2!=0:
            if len(pole_dict['A'])!=0 and pole_dict['A'][0]==1:
                pole_dict['A'].remove(1)
                pole_dict['B'].insert(0,1)
                one_state='B'
                print('A B 1')
            elif len(pole_dict['B'])!=0 and pole_dict['B'][0]==1:
                pole_dict['B'].remove(1)
                pole_dict['C'].insert(0,1)     
                one_state='C'  
                print('B C 1')     
            elif len(pole_dict['C'])!=0 and pole_dict['C'][0]==1:
                pole_dict['C'].remove(1)
                pole_dict['A'].insert(0,1)       
                one_state='A'
                print('C A 1')
        else:
            if len(pole_dict['A'])!=0 and pole_dict['A'][0]==1:
                pole_dict['A'].remove(1)
                pole_dict['C'].insert(0,1)
                one_state='C'
                print('A C 1')
            elif len(pole_dict['B'])!=0 and pole_dict['B'][0]==1:
                pole_dict['B'].remove(1)
                pole_dict['A'].insert(0,1)     
                one_state='A'  
                print('B A 1')     
            elif len(pole_dict['C'])!=0 and pole_dict['C'][0]==1:
                pole_dict['C'].remove(1)
                pole_dict['B'].insert(0,1)       
                one_state='B'
                print('C B 1')

        #first step done
        #stop if solution atained
        if pole_dict['B']==[*range(1,n+1,1)]:
            return None
        #do step 2
        #lock that pole which has one present in it. and consider operations on other 2poles
        if one_state=='A':
            pole2 = 'B'
            pole3='C'
            if len(pole_dict[pole2])==0:
                q=pole_dict[pole3][0]
                pole_dict[pole3].remove(q)
                pole_dict[pole2].insert(0,q)
                print('{} {} {}'.format(pole3,pole2,q))
            elif len(pole_dict[pole3])==0:
                q=pole_dict[pole2][0]
                pole_dict[pole2].remove(q)
                pole_dict[pole3].insert(0,q)
                print('{} {} {}'.format(pole2,pole3,q))
            else:
                if pole_dict[pole2][0]>pole_dict[pole3][0]:
                    q=pole_dict[pole3][0]
                    pole_dict[pole3].remove(q)
                    pole_dict[pole2].insert(0,q)
                    print('{} {} {}'.format(pole3,pole2,q))
                elif pole_dict[pole3][0]>pole_dict[pole2][0]:
                    q=pole_dict[pole2][0]
                    pole_dict[pole2].remove(q)
                    pole_dict[pole3].insert(0,q)
                    print('{} {} {}'.format(pole2,pole3,q))
        
        elif one_state=='B':
            pole2 = 'C'
            pole3='A'
            if len(pole_dict[pole2])==0:
                q=pole_dict[pole3][0]
                pole_dict[pole3].remove(q)
                pole_dict[pole2].insert(0,q)
                print('{} {} {}'.format(pole3,pole2,q))
            elif len(pole_dict[pole3])==0:
                q=pole_dict[pole2][0]
                pole_dict[pole2].remove(q)
                pole_dict[pole3].insert(0,q)
                print('{} {} {}'.format(pole3,pole3,q))
            else:
                if pole_dict[pole2][0]>pole_dict[pole3][0]:
                    q=pole_dict[pole3][0]
                    pole_dict[pole3].remove(q)
                    pole_dict[pole2].insert(0,q)
                    print('{} {} {}'.format(pole3,pole2,q))
                elif pole_dict[pole3][0]>pole_dict[pole2][0]:
                    q=pole_dict[pole2][0]
                    pole_dict[pole2].remove(q)
                    pole_dict[pole3].insert(0,q)
                    print('{} {} {}'.format(pole2,pole3,q))

        elif one_state=='C':
            pole2 = 'A'
            pole3='B'
            if len(pole_dict[pole2])==0:
                q=pole_dict[pole3][0]
                pole_dict[pole3].remove(q)
                pole_dict[pole2].insert(0,q)
                print('{} {} {}'.format(pole3,pole2,q))
            elif len(pole_dict[pole3])==0:
                q=pole_dict[pole2][0]
                pole_dict[pole2].remove(q)
                pole_dict[pole3].insert(0,q)
                print('{} {} {}'.format(pole2,pole3,q))
            else:
                if pole_dict[pole2][0]>pole_dict[pole3][0]:
                    q=pole_dict[pole3][0]
                    pole_dict[pole3].remove(q)
                    pole_dict[pole2].insert(0,q)
                    print('{} {} {}'.format(pole3,pole2,q))
                elif pole_dict[pole3][0]>pole_dict[pole2][0]:
                    q=pole_dict[pole2][0]
                    pole_dict[pole2].remove(q)
                    pole_dict[pole3].insert(0,q)
                    print('{} {} {}'.format(pole2,pole3,q))




if __name__ == "__main__":
    #input should be non neg integer
    hanoi(2)





