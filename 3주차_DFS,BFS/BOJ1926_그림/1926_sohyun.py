# 뭐가 문제 죠...................?????????????????????? 일단 커밋...

# 그림

# <-문제-> 
# 그림 개수 그림 넓이가 가장 넓은 것의 넓이 출력
# 1로 연결 -> 한그림 1의 갯수 = 넓이

# <-알고리즘 구상 -> 
# 가장먼저 든 생각은 상하좌우 쓰자 
# 노드 기준으로 상하좌우 ~ 하고 그 안 노드를 계속 살펴야하니 재귀가 좋겟으니 (dfs)


import sys
input = sys.stdin.readline

n,m = map(int,input().strip().split())

loc = [] # 위치 담을 곳
visited = [[False]*m]*n
_max = 0 # 최대값 담을 곳 ? 

# 상하좌우
dx = [0, 0, -1 ,1] 
dy = [-1, 1 ,0, 0]

for i in range(n):
    loc.append(list(map(int, input().strip().split())))

def dfs(loc,y,x,visited):
    visited[y][x] = True
    global _max
    _max+=1
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if nx<0 or nx>=m or ny<0 or ny>=n:
            continue
        if not visited[ny][nx] and loc[ny][nx]==1:
            dfs(loc,ny,nx,visited)

count =0 
answer = 0
for i in range(n):
    for j in range(m):
        if loc[i][j] == 1 and visited[i][j] == False: #방문하지 않았을때 / 1인 곳
            count+=1
            _max = 0
            dfs(loc,i,j,visited)
            answer = max(answer , _max)

print(count)
print(answer)








