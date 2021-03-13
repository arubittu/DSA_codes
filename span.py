from collections import deque #stack object

def span(arr,n): # main function

    stack1=deque()    #stack to store array elements
    stack2=deque()    # stack to store span of subsequent elements

    stack1.append(arr[0])    #since first element always has span of 1 we append it
    stack2.append(1)
    max_element=arr[0]       #keeping track of the max element in array, if we encounter an element greater than it then we know span.

    for i in range(1,n):     

        if arr[i]<arr[i-1]:
            stack1.append(arr[i])
            stack2.append(1)
        else:
            myspan=1
            j=i-1
            if arr[i]>=max_element:
                max_element=arr[i]
                stack1.append(arr[i])
                stack2.append(i+1)
            else:
                while arr[i]>=arr[j] and j>=0:   
                    myspan=myspan+stack2[j]
                    j=j-stack2[j]               # IMP step, 
                stack1.append(arr[i])
                stack2.append(myspan)
    return stack2


if __name__=='__main__':
     #list=[5,2,4,3,5]
     list=list(range(1,100))
     n=len(list)
     print(span(list,n))
    