# 수 묶기

import sys
input = sys.stdin.readline
n = int(input().strip())
plus = []
minus = []
zero = 0
for _ in range(n):
    i = int(input())
    if i > 0 :
        plus.append(i)
    elif i<0:
        minus.append(i) 
    else:
        zero = 1 # 0은 있는지 없는지만 확인

#둘다 앞부터 보면 되도록 정렬
plus.sort(reverse=True) 
minus.sort() 
sum=0


for i in range(0,len(plus)//2+1,2):
    if(len(plus)<=1):
        break
    sum+=max(plus[i]*plus[i+1],plus[i]+plus[i+1])
    
if(len(plus)%2 == 1):
    sum+=plus[len(plus)-1] # 홀수일 경우 마지막 요소 더해줌


for i in range(0,len(minus)//2+1,2):
    if(len(minus)<=1):
        break
    sum+=minus[i]*minus[i+1]
if(len(minus)%2 == 1):
    if(zero==0):
        sum+=minus[len(minus)-1] # 홀수일 경우 마지막 요소 더해줌 / 0 고려

print(sum)


