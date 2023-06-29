# 큐에 (우선순위, 인덱스) 로 저장 후 문제 설명 그대로 구현

from collections import deque

def isBigger(queue):
    queue_list = list(queue)
    start = queue_list[0][0]

    for i in range(1,len(queue_list)):
        if start < queue_list[i][0]: return True
    return False

t = int(input())

for _ in range(t):
    n,m = map(int,input().split())
    docs = list(map(int,input().split()))
    answer = 0

    queue = deque()
    for i in range(n):
        queue.append((docs[i],i))
    
    while queue:
        if isBigger(queue) == True: queue.append(queue.popleft())
        else:
            num,idx = queue.popleft()
            answer += 1
            if idx == m:
                print(answer)
                break
    