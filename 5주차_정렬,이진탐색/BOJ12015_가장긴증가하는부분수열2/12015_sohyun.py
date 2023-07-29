import sys

input=sys.stdin.readline()
n=int(input())
a=list(map(int,input()))
init=[0]
 
for i in range(n):
 
    low=0
    high=len(init)-1

    while low<=high:
        mid=(low+high)//2
        if init[mid]<a[i]:
            low=mid+1
        else:
            high=mid-1
 
    if low>=len(init):
        init.append(a[i])
    else:
        init[low]=a[i]
 
print(len(init)-1)
