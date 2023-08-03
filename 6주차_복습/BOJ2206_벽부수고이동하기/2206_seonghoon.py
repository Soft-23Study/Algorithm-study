from collections import deque
n, m = map(int, input().split())

maze = []
visited = [[[0]*2 for _ in range(m)] for j in range(n)]

for _ in range(n):
    row = list(map(int, input()))
    maze.append(row)

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs():
    queue = deque()
    queue.append((0, 0, 0))
    visited[0][0][0] = 1
    while queue:
        x, y, z = queue.popleft()

        if x == n-1 and y == m-1:
            return visited[x][y][z]

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                continue

            if maze[nx][ny] == 0 and visited[nx][ny][z] == 0: ## 벽이 아니고, 방문했던 곳이 아닐 경우
                visited[nx][ny][z] = visited[x][y][z] + 1
                queue.append((nx, ny, z))
            elif maze[nx][ny] == 1 and z == 0: ## 벽이고, 부술 기회가 있을 경우
                visited[nx][ny][1] = visited[x][y][z] + 1
                queue.append((nx, ny, 1))

    return -1


print(bfs())
# dfs는 시간초과.. bfs로 생각해야 한다.

# import copy
#
# n, m = map(int, input().split())
#
# maze = []
# visited = [[False for i in range(m)] for j in range(n)]
# for _ in range(n):
#     row = list(map(int, input()))
#     maze.append(row)
#
# x = 0; y = 0
#
# dx = [-1, 1, 0, 0]
# dy = [0, 0, -1, 1]
#
# answer = 2001
#
# def dfs(x, y, visited, already_broke, length):
#     if x < 0 or x >= n or y < 0 or y >= m or visited[x][y]:
#         return
#
#     if maze[x][y] == 1:
#         if already_broke:
#             return
#         already_broke = True
#
#     visited[x][y] = True
#     length += 1
#
#     global answer
#
#     if x == n-1 and y == m-1:
#         answer = min(answer, length)
#
#     for i in range(4):
#         dfs(x+dx[i], y+dy[i], copy.deepcopy(visited), already_broke, length)
#
# dfs(0, 0, visited, False, 0)
# if answer == 2001:
#     print(-1)
# else:
#     print(answer)