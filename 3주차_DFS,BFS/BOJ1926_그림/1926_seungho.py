# starting time: 23:04
# finish time : 23:54

'''
bfs로도 풀리고, dfs로도 풀리겠지만
하나의 덩어리를 찾아야하는 문제임을 보고 dfs로 풀기로 판단.

빠르게 정답맞을줄 알았지만 틀렸습니다 판정받고 어디서 틀렸는지를 보느라 시간 많이씀.
보니까 함수 정의 시 return을 남발하여 겉으로는 돌아가는 듯 해도 접근 안하는 노드가 있음을 발견하고,
재귀를 넣어줄 땐 return쓰지 않고 마지막에만 return해주는 코드로 수정.
또한 global 변수로 size를 둬서 해당 덩어리의 넓이 누적하는 방향으로 변경

허나, RecursionError가 떠서 찾아보니
sys.setrecursionlimit(max_limit) 함수를 쓰면 예외처리해준다는 것을 알았다.
n, m 모두 최대 500이라서 500*500=250000번의 recursion을 허용해주니까 정답 판정.
'''
import sys
sys.setrecursionlimit(250000)
input = sys.stdin.readline

n, m = map(int, input().strip().split())
paper = []
visited = [[False] * m for _ in range(n)]
size = 0
dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]


def dfs(graph, y, x, visited):
    global size
    visited[y][x] = True
    size += 1

    for i in range(4):
        ny, nx = y + dy[i], x + dx[i]
        if ny < 0 or ny >= n or nx < 0 or nx >= m:
            continue
        if visited[ny][nx] == False and graph[ny][nx] == 1:
            dfs(graph, ny, nx, visited)



for i in range(n):
    paper.append(list(map(int, input().strip().split())))

max_size = 0
cnt = 0
for i in range(n):
    for j in range(m):
        if paper[i][j] == 1 and visited[i][j] == False:
            cnt += 1
            size = 0
            dfs(paper, i, j, visited)
            max_size = max(max_size, size)

print(cnt)
print(max_size)