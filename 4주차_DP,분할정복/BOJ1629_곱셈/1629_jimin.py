a,b,c = map(int,input().split())

def calc(a,n):    # a^n % c 계산
    if n==1:
        return a%c
    else:
        tmp = calc(a,n//2)
        if n%2 == 0:                        
            return (tmp*tmp)%c
        else:
            return (tmp*tmp*a)%c
        
print(calc(a,b)) 