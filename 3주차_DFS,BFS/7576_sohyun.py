# 토마토

# 상하좌우 + bfs

import sys
from collections import deque

input = sys.stdin.readline

dx = [0, 0, -1 ,1] 
dy = [-1, 1 ,0, 0]

m, n = map(int, input().split())
tomato = []
for i in range(n):
    tomato.append(list(map(int, input().strip().split())))
queue = deque([])

for i in range(n):
    for j in range(m):
        if tomato[i][j] == 1:
            queue.append((i, j))

while queue:
    x, y = queue.popleft()
    for k in range(4):
        nx = x + dx[k]
        ny = y + dy[k]
        
        if nx<0 or nx>=n or ny<0 or ny>=m or tomato[nx][ny] != 0:
            continue
        
        tomato[nx][ny] = tomato[x][y] + 1
        queue.append((nx, ny))

answer = max(map(max, tomato)) - 1
for a in tomato:
    if 0 in a:
        answer = -1

print(answer)
