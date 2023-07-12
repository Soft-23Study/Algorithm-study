'''
처음엔 dfs로 풀려고 했으나,
1일차에 여러개의 1번 토마토들이 라운드로빈처럼 하나씩 퍼지는 형식이기 때문에 bfs로 전략 변경.
골드5치고 쉬웠다.
'''

import sys
from collections import deque

input = sys.stdin.readlin다

m, n = map(int, input().strip().split())
box = [[-1]*(m+1) for _ in range(n+1)]
visited = [[False]*m for _ in range(n)]

queue = deque([])
answer = 0
day = 0
dy = [-1,1,0,0]
dx = [0,0,-1,1]

for i in range(1,n+1):
    temp = list(map(int, input().strip().split()))
    for j in range(1,m+1):
        box[i][j] = temp[j-1]
        if box[i][j] == 1:
            queue.append([i, j, day])
if len(queue) == 0:
    answer = 0 #익은 토마토 1개도 없으면 정답 0처리

while queue:
    cur_y, cur_x, cur_day = queue.popleft()
    answer = max(answer, cur_day)
    for i in range(4):
        ny, nx = cur_y+dy[i], cur_x+dx[i]
        if ny<=0 or ny>n or nx<=0 or nx>m:
            continue
        if box[ny][nx] == -1 or box[ny][nx] == 1:
            #벽이거나 토마토 없는곳이거나 익은토마토 있는 곳일 때
            continue
        queue.append([ny, nx, cur_day+1])
        box[ny][nx] = 1

for line in box:
    if 0 in line:
        answer = -1
print(answer)
