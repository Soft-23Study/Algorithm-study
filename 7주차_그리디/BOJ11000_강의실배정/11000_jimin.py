# ---------------------------------------------------- 1트 => 2% 에서 실패. deque 으로 하면 안됨 + sort 틀림
# from collections import deque

# n = int(input())
# arr = []
# for _ in range(n):
#     arr.append(list(map(int,input().split())))

# arr.sort(key = lambda x: (x[1],x[0]))

# answer = 1
# queue = deque([arr[0][1]])

# for i in range(1,n):
#     if arr[i][0] < queue[0]:
#         answer += 1
#         queue.append(arr[i][1])
#     else:
#         queue.popleft()
#         queue.append(arr[i][1])

# print(answer)


# ---------------------------------------------------- 2트 => 답 참고
# 1. 1트에서 deque -> heapq 으로 바꿔줬으나, 똑같이 2% 에서 실패해서 답 참고
# 2. 답과 나의 차이점: 나는 "종료시간" 을 우선으로 정렬, 답은 "시작시간" 을 기준으로 정렬.. 상관있나?
# ---------------------------------------------------- 
import heapq

n = int(input())
arr = []
for _ in range(n):
    arr.append(list(map(int,input().split())))

# arr.sort(key = lambda x: (x[1],x[0]))      -> 이렇게 하면 틀림. why ???
arr.sort()

answer = 1
p_q = []
heapq.heappush(p_q,arr[0][1])

for i in range(1,n):
    if arr[i][0] < p_q[0]:
        answer += 1
        heapq.heappush(p_q,arr[i][1])
    else:
        heapq.heappop(p_q)
        heapq.heappush(p_q,arr[i][1])

print(answer)
