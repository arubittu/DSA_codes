# aryan kolapkar
# 190260010
# aryan_kolapkar


def findMaxima(n,min,max,xor): # n is the np array
   # if min>=max:
    #    return False
    if xor^n[min]>=xor^n[min+1]:
        return min+1
    if xor^n[max]>=xor^n[max-1]:
        return max+1
    elif xor^n[((min+max)//2)-1]<=xor^n[(min+max)//2]>=xor^n[((min+max)//2)+1]:
        return ((min+max)//2)+1
    elif xor^n[(min+max)//2]<=xor^n[((min+max)//2)+1]:
        return findMaxima(n,((min+max)//2)+1,max,xor)
    else:# n[((min+max)//2)-1]>=n[(min+max)//2]:
        return findMaxima(n,min,((min+max)//2)-1,xor)

def solution(n,x,no_x): # n is list of integers and x is the list of x to multiply everytime
    xor_num=0
    for i in range(no_x):
        #if x[i]>0:
        #n= [x[i]^a for a in n]
        xor_num=xor_num^x[i]
        position=findMaxima(n,0,len(n)-1,xor_num)#x[:i+1])
         
        print(position)

if __name__=='__main__':
    i=input()
    array=input()
    i=list(map(int,list(i.split(None))))
    array=list(map(int,list(array.split(None)))) 
    no_elements=i[0]
    no_x=i[1]
    x=[]
    for p in range(no_x):
        num=int(input())
        x.append(num)
    solution(array,x,i[1])

