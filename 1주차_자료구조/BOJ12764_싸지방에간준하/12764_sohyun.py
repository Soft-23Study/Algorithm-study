#싸지방에 간 준하

# 컴퓨터가 있는 자리 1~ 순서대로 번호
# 비어있는 자리 중 번호가 가장 작은 자리에 앉는 것이 규칙

# 모든 사람은 항상 정해진 시간에 싸지방 이용

# 모든 사람이 기다리지 않고 싸지방을 이용할 수있는 컴퓨터 최소갯수
# 자리별로 몇명의 사람이 사용했는지 구하라

#1st 최소힙 -> 시간 초과 떴었음
# pypy3으로 언어 사용한걸로 돌리면 성공 이긴한데 메모리가 131048로
# 다른 분들이 사용한 방식의 메모리보다 2배 이상 사용됨  
import sys
import heapq

N = int(sys.stdin.readline())

heap = []
computers = [0]*N
count = [0]*N
# computers = [0 for _ in range(N)]
# count = [0 for _ in range(N)]

num = 0

for i in range(N):
    P,Q = map(int,sys.stdin.readline().split()) # 이용시작시각 ~ 종료시각
    heapq.heappush(heap, [P,Q]) # 최소힙

while heap : 
    used = heapq.heappop(heap)
    for i in range(N):
        if computers[i] <= used[0]:
            if computers[i] == 0 :
                num+=1
            computers[i]=used[1]
            count[i]+=1
            break

print(num)
for i in count:
        if i != 0:
            print(i, end= " ")


# 첨부)  메모리 60000정도 쓰이는 알고리즘
# 구현 방식은 비슷한데 추가로 deque를 사용
# import sys
# import heapq
# from collections import deque

# START, END = 0, 1
# N = int(sys.stdin.readline().strip())
# time_set = [list(map(int, sys.stdin.readline().split()))for _ in range(N)]
# time_set.sort(key=lambda x: (x[START], x[END]))
# time_set = deque(time_set)
# computers = []      #heap
# empty = [i for i in range(N)]
# heapq.heapify(empty)            #사용할 수 있는 컴퓨터
# tick = -1
# count = [0 for _ in range(N)]
# answer = [0]            # 0번은 갯수 1번부터 사용한 횟수

# while time_set:
#     tick += 1
#     if tick == time_set[0][START]:
#         temp = time_set.popleft()
#         idx = heapq.heappop(empty)
#         heapq.heappush(computers, [temp[END], temp[START], idx])
#         count[idx] += 1
#     if computers and computers[0][0] == tick:
#         s, e, i = heapq.heappop(computers)
#         heapq.heappush(empty, i)

# for i in count:
#     if i == 0:
#         break
#     else:
#         answer.append(i)
#         answer[0] += 1

# print(answer[0])
# print(*answer[1:])
