# 인구 이동

# <-문제->
# N,N / A[r][c]명 살고 있음 -> 인구 이동 없을때까지
# BFS

from collections import deque
import sys
input = sys.stdin.readline

n, l, r = map(int, sys.stdin.readline().split())


loc = []
for _ in range(n):
    loc.append(list(map(int, sys.stdin.readline().split())))

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

answer = 0

def process(x, y, union_number):
    con = []
    con.append((x, y))

    q = deque()
    q.append((x, y))
    union[x][y] = union_number

    unit = loc[x][y]
    count = 1

    while q:
        now = q.popleft()
        for k in range(4):
            nx = now[0] + dx[k]
            ny = now[1] + dy[k]
            if ny<0 or ny>=n or nx<0 or nx>=n: continue
            if (union[nx][ny] == -1 and  l <= abs(loc[nx][ny] - loc[now[0]][now[1]]) <= r ):
                union[nx][ny] = union_number
                q.append((nx, ny))
                unit += loc[nx][ny]
                count += 1
                con.append((nx, ny))

    for i, j in con:
        loc[i][j] = unit // count #나머지 버리기

while True:    
    union = [[-1]*n for _ in range(n)]
    union_number = 0

    for i in range(n):
        for j in range(n):
            if (union[i][j] == -1):
                process(i, j, union_number)
                union_number += 1
                
    if (union_number == n*n):
        break
    answer += 1

print(answer)
