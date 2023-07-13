# ----------------------------------------------------
# 재귀 사용 시 sys.setrecursionlimit 꼭 써주고 시작하자 !!!!
# ----------------------------------------------------
import sys
sys.setrecursionlimit(10**6)

n,m = map(int,input().split())
_map = []
for _ in range(n):
    _map.append(list(map(int,input().split())))

dx = [-1,0,1,0]
dy = [0,-1,0,1]

visited = [[False] * m for _ in range(n)]

def dfs(cur_x,cur_y):
    global area

    visited[cur_x][cur_y] = True
    area += 1

    for i in range(4):
        next_x, next_y = cur_x + dx[i], cur_y + dy[i]

        if next_x<0 or next_x>=n or next_y<0 or next_y>=m: continue
        
        if _map[next_x][next_y] == 1 and not visited[next_x][next_y]:
            dfs(next_x,next_y)

drawings = []
area = 0

for i in range(n):
    for j in range(m):
        if _map[i][j] == 1 and not visited[i][j]:
            area = 0
            dfs(i,j)
            drawings.append(area)

print(len(drawings))
if len(drawings) == 0: print(0)
else: print(max(drawings))
