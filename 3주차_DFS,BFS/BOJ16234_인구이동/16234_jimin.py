 # 연합마다 bfs 돌리며 연합의 인구 수 구하기 -> 인구이동 후 결과 인구 수 구해서 update

from collections import deque

n,l,r = map(int,input().split())
_map = []
for _ in range(n):
    _map.append(list(map(int,input().split())))

dx = [-1,0,1,0]
dy = [0,-1,0,1]

answer = 0

def bfs(start_x,start_y,visited):
    queue = deque([(start_x,start_y)])
    visited[start_x][start_y] = True

    unions = []              # (x,y,_map[x][y])
    unions.append((start_x,start_y,_map[start_x][start_y]))

    while queue:
        cur_x, cur_y = queue.popleft()
      
        for i in range(4):
            next_x, next_y = cur_x + dx[i], cur_y + dy[i]

            if next_x<0 or next_x>=n or next_y<0 or next_y>=n: continue
            if abs(_map[cur_x][cur_y]-_map[next_x][next_y])<l or abs(_map[cur_x][cur_y]-_map[next_x][next_y])>r: continue

            if not visited[next_x][next_y]:
                queue.append((next_x,next_y))
                visited[next_x][next_y] = True
                unions.append((next_x,next_y,_map[next_x][next_y]))

    return unions


while True:
    # 국경선 열기
    all_unions = []
    visited = [[False]*n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if not visited[i][j]: 
                _unions = bfs(i,j,visited)
                if len(_unions) > 1: all_unions.append(_unions)

    if len(all_unions) == 0:
        print(answer)
        exit()

    # 인구 이동
    for unions in all_unions:
        total_people = 0
        for area in unions: total_people += area[2]
        result_people = total_people // len(unions)
        for area in unions: _map[area[0]][area[1]] = result_people

    answer += 1