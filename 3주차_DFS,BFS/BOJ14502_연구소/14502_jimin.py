# 배열 복사 까먹지말자 !!! => copy.deepcopy(arr)

from collections import deque
from itertools import combinations
import copy

n,m = map(int,input().split())
_map = []
for _ in range(n):
    _map.append(list(map(int,input().split())))

virus = []
empty = []
for i in range(n):
    for j in range(m):
        if _map[i][j] == 0: empty.append((i,j))
        elif _map[i][j] == 2: virus.append((i,j))

candi_walls = combinations(empty,3)

dx = [-1,0,1,0]
dy = [0,-1,0,1]

def bfs(walls):
    queue = deque(virus)

    while queue:
        cur_x, cur_y = queue.popleft()
        
        for i in range(4):
            next_x, next_y = cur_x + dx[i], cur_y + dy[i]

            if next_x<0 or next_x>=n or next_y<0 or next_y>=m: continue
            if (next_x,next_y) in walls: continue

            if temp_map[next_x][next_y] == 0:
                temp_map[next_x][next_y] = 2
                queue.append((next_x,next_y))

def check_safe(walls):
    cnt = 0
    for i in range(n):
        for j in range(m):
            if (i,j) in walls: continue
            if temp_map[i][j] == 0: cnt += 1
    return cnt

answer = 0
for walls in candi_walls:
    temp_map = copy.deepcopy(_map)
    bfs(walls)
    answer = max(answer,check_safe(walls))

print(answer)