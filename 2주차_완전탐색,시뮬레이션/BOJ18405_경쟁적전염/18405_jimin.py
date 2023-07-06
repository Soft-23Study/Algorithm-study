# ----------------------------------------------------
# 1. bfs 를 돌리되, 큐에 '오늘 전파할 바이러스 리스트' 를 넣어서 돌리는게 핵심
# 2. '오늘 전파할 바이러스 리스트' 배열 == (바이러스 넘버, 행, 열) 들의 리스트
#     => sort 로 바이러스 넘버가 적은 순으로 정렬 가능!
# 3. 백준 7576(토마토) 랑 비슷한 문제. 분명 어디서 봤던 문젠걸 알면서 시작할때 좀 헤맨 느낌. 반성하자 !!!
# ----------------------------------------------------
from collections import deque

n,k = map(int,input().split())
_map = []
for _ in range(n):
    _map.append(list(map(int,input().split())))
s,x,y = map(int,input().split())

time = 0

start_virus = []
for i in range(n):
    for j in range(n):
        if _map[i][j] > 0: start_virus.append((_map[i][j],i,j))

dx = [-1,0,1,0]
dy = [0,-1,0,1]

def bfs(start_virus):
    global time
    queue = deque()
    queue.append(start_virus)

    while queue and time<s:
        today_virus = queue.popleft()
        today_virus.sort()
        next_day_virus = []

        for num, cur_x, cur_y in today_virus:
            for i in range(4):
                next_x, next_y = cur_x + dx[i], cur_y + dy[i]
                if next_x<0 or next_x>=n or next_y<0 or next_y>=n: continue
                if _map[next_x][next_y] == 0:
                    _map[next_x][next_y] = num
                    next_day_virus.append((num,next_x,next_y))

        queue.append(next_day_virus)
        time += 1

bfs(start_virus)

print(_map[x-1][y-1])






