def solve(A,n):## change to s maybe
    """
    Complete this function ..!
    """
    B=[None]*(len(A)//2)
    for i in range(len(B)): #power of 2 is n
        B[i]=A[2*i]+A[2*i+1]
    if len(B)==1:
        return B[0]
    else:
        solve(B,n//2)
    
        
if __name__=='__main__':
    n = 4#int(input())
    A = [2,2,2,2]#list(map(int, input().split()))
    print(solve(A,n))
