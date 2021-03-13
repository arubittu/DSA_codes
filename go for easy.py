
def ways(n,x,y):
    if x==y==n:
        return 1
    elif x==y:
        return ways(n,x+1,y)
    elif x>y:
        if x==n:
            return ways(n,x,y+1)
        else:
            return ways(n,x+1,y)+ways(n,x,y+1)


if __name__=='__main__':
    n=int(input())
    print(ways(n,0,0))
 
