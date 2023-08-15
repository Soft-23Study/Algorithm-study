# 강의실 배정

import sys
import heapq

input = sys.stdin.readline
arr = []
heap = []
answer = 1

n = int(input())
for _ in range(n):
    arr.append(list(map(int, input().split()))) # 시작 시간 , 종료 시간
arr.sort()

heapq.heappush(heap,arr[0][1]) # 맨 처음의 강의의 종료 시간 넣어 놓음

for i in range(1, n):
    v = heapq.heappop(heap)
    
    # 종료 시간과 시작 시간 비교
    if v > arr[i][0]:
        answer+=1 # 강의실 추가
        heapq.heappush(heap,arr[i][1])
        heapq.heappush(heap,v)
    else :
        heapq.heappush(heap,arr[i][1])


print(answer)
