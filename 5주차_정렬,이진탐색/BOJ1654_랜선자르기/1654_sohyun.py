# 랜선 자르기
# 이분탐색인걸 알고 풀어서 쉬운 문제 

import sys
input = sys.stdin.readline

k,n = map(int,input().split()) 

lines = [int(input()) for _ in range(k)]

start,end = 1, max(lines)

while start <= end :
    mid = (start+end)//2 # 중간 값

    answer=0
    for i in lines:
        answer+=i//mid

    if answer >= n:
        # 갯수가 많은 경우는 값을 올려서 봐야지
        start = mid + 1
    else:
        # 갯수가 작은 경우는 왼쪽(작은 값)
        end= mid -1
#최대 랜선 길이      
print(end)
