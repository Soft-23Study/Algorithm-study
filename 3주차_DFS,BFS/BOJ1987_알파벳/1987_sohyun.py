# 알파벳

# <-문제->

# 세로 R 가로 C 
# 대문자 알파벳 / 1,1 말
# 상하좌우
# 이동한 칸 = 모든 알파벳과 다르게
# 최대 이동할 수 있는 칸 수

# 알고리즘 구상
# 무조건 dfs 라고 생각했는데 시간 초과 나는거보니 bfs도 구현 해봐야겠다고 생각듦
# 구글링으로 
# 람다 -> 아스키코드 바꾸는 방식 으로 시간 초과 해결 /pypy3으로 해결.. python에서 시간 초과 어떻게 해야안나죵..?

import sys
input = sys.stdin.readline

R,C = map(int,input().strip().split())
# loc = []
visited = [0]*26
# for i in range (R):
#     loc.append(list(input()))

#람다 -> 아스키코드 바꾸는 방식
loc = [list(map(lambda x: ord(x)-65, sys.stdin.readline().rstrip())) for _ in range(R)] 

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

print(loc)
count = 1

def dfs(loc, x,y,visited,new):
    global count
    count = max(count, new)
    for i in range(4):
        nx=x+dx[i]
        ny=y+dy[i]
        if ny<0 or ny>=R or nx<0 or nx>=C:
            continue
        print(loc[nx][ny],nx,ny)
        if visited[loc[nx][ny]]==0:
            visited[loc[nx][ny]] = 1
            dfs(loc,nx, ny, visited , new+1) # 재귀적으로 dfs 탐색
            visited[loc[nx][ny]] = 0
        
visited[loc[0][0]] = 1
dfs(loc,0,0,visited,1)
