'''
미완성 풀이 -> 방법은 맞는거같은데 미세한 구현에서 틀린것 같다. 일단 올리고...
'''

import sys
from itertools import combinations
from collections import deque

sys.setrecursionlimit(1000)
input = sys.stdin.readline

n, m = map(int, input().strip().split())
lab = original_lab = [[-1]*(m+1) for _ in range(n+1)]
virus_case = []
walls_case = []

dy = [-1,1,0,0]
dx = [0,0,-1,1]

safe_size = 0
size = 0

for i in range(1,n+1):
    temp = list(map(int, input().strip().split()))
    for j in range(1,m+1):
        lab[i][j] = original_lab[i][j] = temp[j-1]
        if lab[i][j] == 0:
            walls_case.append((i,j))
        if lab[i][j] == 2:
            virus_case.append((i,j))

for walls in list(combinations(walls_case, 3)):
    queue = deque([])
    #현재 시뮬레이션 맵 초기화
    for i in range(1, n+1):
        for j in range(1, m+1):
            lab[i][j] = original_lab[i][j]
    # 초기 바이러스 큐에 추가
    for virus in virus_case:
        queue.append((virus[0], virus[1]))
    # 해당 벽 케이스들을 랩 지도에 추가
    for wall in walls:
        wall_y, wall_x = wall[0], wall[1]
        lab[wall_y][wall_x] = 1

    #메인 루프
    while queue:
        cur_y, cur_x = queue.popleft()
        for i in range(4):
            ny, nx = cur_y+dy[i], cur_x+dx[i]
            if ny<=0 or ny>n or nx<=0 or nx>n:
                continue
            if lab[ny][nx] == 0:
                lab[ny][nx] = 2
                queue.append((ny, nx))
    size = 0
    for i in range(1,n+1):
        for j in range(1, m+1):
            if lab[i][j] == 0:
                size += 1
    safe_size = max(safe_size, size)
print(safe_size)