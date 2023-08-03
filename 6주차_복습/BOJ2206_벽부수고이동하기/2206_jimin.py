# ---------------------------------------------------- 1트 => 시간초과 (dfs)
# import sys
# sys.setrecursionlimit(10**6)

# n,m = map(int,input().split())
# _map = []
# for _ in range(n):
#     _map.append(list(map(int,input())))

# dx = [-1,0,1,0]
# dy = [0,-1,0,1]

# visited = [[False]*m for _ in range(n)]
# answer = 1e9
# crashed = [-1,-1]

# def dfs(cur_x,cur_y,cnt):
#     global answer

#     visited[cur_x][cur_y] = True

#     if cur_x == n-1 and cur_y == m-1: 
#         answer = min(answer,cnt)
#         return
    
#     for i in range(4):
#         next_x, next_y = cur_x + dx[i], cur_y + dy[i]

#         if next_x<0 or next_x>=n or next_y<0 or next_y>=m: continue

#         if crashed[0] == -1 and _map[next_x][next_y] == 1:
#             _map[next_x][next_y] = 0
#             crashed[0], crashed[1] = next_x, next_y
        
#         if not visited[next_x][next_y] and _map[next_x][next_y] == 0:
#             dfs(next_x,next_y,cnt+1)
         
#     if crashed[0] != -1:
#         _map[crashed[0]][crashed[1]] = 1
#         crashed[0], crashed[1] = -1,-1
        
#     visited[cur_x][cur_y] = False
        
# dfs(0,0,1)

# if answer == 1e9: print(-1)
# else: print(answer)


# ---------------------------------------------------- 2트 => 18% 에서 틀림 (bfs)
# 1. 현재 이동 경로에서 벽을 파괴할 수 있는지 여부를 flag 변수로 관리
# 2. 0000
#    0100
#    1111
#    0000 같은 경우에, "2행4열 -> 벽 부수기 -> 목적지 도착" 으로 갈수 있는데 2행2열 벽을 먼저 부숴버리면 정답을 못찾는 문제점
# ----------------------------------------------------
# from collections import deque

# n,m = map(int,input().split())
# _map = []
# for _ in range(n):
#     _map.append(list(map(int,input())))

# dx = [-1,0,1,0]
# dy = [0,-1,0,1]

# visited = [[False]*m for _ in range(n)]
# answer = 1e9

# def bfs(start_x,start_y,start_cnt):
#     global answer

#     queue = deque([(start_x,start_y,start_cnt,True)])
#     visited[start_x][start_y] = True

#     while queue:
#         cur_x, cur_y, cnt, flag = queue.popleft()

#         if cur_x == n-1 and cur_y == m-1:
#             answer = min(answer,cnt)
    
#         for i in range(4):
#             next_x, next_y = cur_x + dx[i], cur_y + dy[i]

#             if next_x<0 or next_x>=n or next_y<0 or next_y>=m: continue

#             if flag == True and _map[next_x][next_y] == 1 and not visited[next_x][next_y]:
#                 queue.append((next_x,next_y,cnt+1,False))
#                 visited[next_x][next_y] = True
        
#             if not visited[next_x][next_y] and _map[next_x][next_y] == 0:
#                 queue.append((next_x,next_y,cnt+1,flag))
#                 visited[next_x][next_y] = True
        
# bfs(0,0,1)

# if answer == 1e9: print(-1)
# else: print(answer)


# ---------------------------------------------------- 3트 => 답 참고
# 1. 위 문제 때문에 '현위치까지 벽을 부수고 오는 경우(wall_break=0)' 와 그렇지 않은 경우 (wall_break=1) 로 관리
#    => 3차원 배열 필요
# ----------------------------------------------------
from collections import deque

n,m = map(int,input().split())
_map = []

visited = [[[0]*2 for _ in range(m)] for _ in range(n)]
visited[0][0][0] = 1

for i in range(n):
    _map.append(list(map(int,input())))

dx = [0,-1,0,1]
dy = [-1,0,1,0]

def bfs(start_x,start_y):
    queue = deque()
    queue.append((start_x,start_y,False))

    while queue:
        cur_x, cur_y, flag = queue.popleft()

        if cur_x == n-1 and cur_y == m-1:
            return visited[cur_x][cur_y][flag]

        for i in range(4):
            next_x = cur_x + dx[i]
            next_y = cur_y + dy[i]

            if next_x<0 or next_x>=n or next_y<0 or next_y>=m: continue

            if _map[next_x][next_y] == 1 and flag == False:
                visited[next_x][next_y][1] = visited[cur_x][cur_y][0] + 1
                queue.append((next_x,next_y,1))
            elif _map[next_x][next_y] == 0 and visited[next_x][next_y][flag] == 0:
                visited[next_x][next_y][flag] = visited[cur_x][cur_y][flag] + 1
                queue.append((next_x,next_y,flag))
    return -1

print(bfs(0,0))
            