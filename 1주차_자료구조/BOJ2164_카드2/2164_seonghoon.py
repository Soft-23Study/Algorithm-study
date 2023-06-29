
## 시간 초과 ##
# import queue
#
# n = int(input())
# queue = queue.Queue()
# for i in range(1, n+1):
#     queue.put(i)
#
# # n이 1일 경우 answer = 1
# answer = 1
#
# while n > 1:
#     # 카드를 버림
#     queue.get()
#
#     # 맨 위 카드를 아래에 추가
#     top = queue.get()
#     if queue.empty():
#         answer = top
#         break
#     queue.put(top)
#
# print(answer)


## 200 ms ##
from collections import deque
n = int(input())
queue = deque(range(1, n+1))
while len(queue) > 1:
    queue.popleft()
    queue.append(queue.popleft())
print(queue[0])