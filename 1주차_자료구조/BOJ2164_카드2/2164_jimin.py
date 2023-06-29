# 위로 빼기 + 밑으로 넣기 둘다 해야되므로 deque 사용
# queue 에 원소 하나 남을때까지 작업 수행 후, 마지막 꺼 pop 해서 출력해주면 답

from collections import deque

n = int(input())

queue = deque()
for i in range(1,n+1): queue.append(i)

while len(queue) > 1:
    queue.popleft()
    queue.append(queue.popleft())

print(queue.popleft())


