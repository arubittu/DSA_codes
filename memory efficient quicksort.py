
def quicksort(arr,p,r):
    while p<r:
        q = PARTITION(arr,p,r)
        if q-p<r-q:
            quicksort(arr,p,q-1)
            p=q+1
        else:
            quicksort(arr,q+1,r)
            r=q-1
    return arr

def PARTITION(arr,p,r):
    x=arr[r]
    i=p-1
    for j in range(p,r):
        if arr[j]<=x:
            i=i+1
            arr[i],arr[j]=arr[j],arr[i]
    arr[i+1],arr[r]=arr[r],arr[i+1]
    return i+1
if __name__ == "__main__":
    #arr=input()
   # print(quicksort([2,1,5,8,4],0,4))
    arr='2 2 22 52 7'
    arr=list(map(int,list(arr.split(None))))
    print('input array is {}'.format(arr))
    print(quicksort(arr,0,len(arr)-1))