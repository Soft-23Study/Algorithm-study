# ----------------------------------------------------
# 2차원 배열에서 최댓값 찾는 법 까먹지 말자 !!!
# ----------------------------------------------------
from collections import deque

m,n = map(int,input().split())
_map = []
for _ in range(n):
    _map.append(list(map(int,input().split())))

dx = [-1,0,1,0]
dy = [0,-1,0,1]

def bfs():
    queue = deque(start)

    while queue:
        cur_x, cur_y = queue.popleft()

        for i in range(4):
            next_x, next_y = cur_x + dx[i], cur_y + dy[i]

            if next_x<0 or next_x>=n or next_y<0 or next_y>=m: continue
            if _map[next_x][next_y] != 0: continue

            _map[next_x][next_y] = _map[cur_x][cur_y] + 1
            
            queue.append((next_x,next_y))

start = []
for i in range(n):
    for j in range(m):
        if _map[i][j] == 1: start.append((i,j))

bfs()

for i in range(n):
    for j in range(m):
        if _map[i][j] == 0:
            print(-1)
            exit()

print(max(map(max,_map))-1)


# 23.03.28 풀이
# ----------------------------------------------------
# 1. today_tomatos : 오늘 익는 토마토들의 배열 / tomorrow_tomatos : 내일 익을 토마토들의 배열
#    => queue 에 이 배열들을 넣어서 관리했음
# 2. day : 날짜 카운트
# 3. [로직] 다음날 익게 될 토마토들을 tomorrow_tomatos 배열에 추가하고 -> 큐에 넣은 뒤 -> 다음 날 되면 큐에서 뽑고 -> 날짜 증가시키기
# [ 회고 ]
# 왜 이리 품? 걍 _map 에 익게 되는 날짜 하나씩 증가시키면서 bfs 돌리면 되는 것.
# ----------------------------------------------------
# from collections import deque
# m,n = map(int,input().split())
# _map = []
# for _ in range(n):
#     _map.append(list(map(int,input().split())))

# dx = [0,-1,0,1]
# dy = [1,0,-1,0]

# def bfs(starting):
#     global day
#     queue = deque()
#     queue.append(starting)

#     while queue:
#         today_tomatos = queue.popleft()
#         day += 1
#         tomorrow_tomatos = []
#         for (cur_x,cur_y) in today_tomatos:
#             for i in range(4):
#                 next_x = cur_x + dx[i]
#                 next_y = cur_y + dy[i]

#                 if next_x<0 or next_x>=m or next_y<0 or next_y>=n: continue
            
#                 if _map[next_y][next_x] == 0:
#                     _map[next_y][next_x] = 1
#                     tomorrow_tomatos.append((next_x,next_y))

#         if len(tomorrow_tomatos) != 0:
#             queue.append(tomorrow_tomatos)
                    
# day = -1

# starting = []
# for y in range(n):
#     for x in range(m):
#         if _map[y][x] == 1:
#             starting.append((x,y))

# bfs(starting)

# for y in range(n):
#     for x in range(m):
#         if _map[y][x] == 0:
#             day = -1

# print(day)
