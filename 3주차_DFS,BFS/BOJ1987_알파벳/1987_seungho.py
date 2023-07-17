'''
문제난이도는 골드4치고는 쉬웠으나,
시간초과를 해결하는 방법이 골드4인듯 하다.

풀이를 보니 리스트를 in으로 통해 조회하는 과정에서 O(N)이 걸리기 때문에 시간을 잡아먹은 듯 하다.
따라서 리스트에 추가 / 삭제하는 방식을 버리고, 0~25번 인덱스에 맞게끔 아스키코드 변환 플래그 방식을 사용하니 돌아간다.

'''
import sys

input = sys.stdin.readline
sys.setrecursionlimit(400)

r, c = map(int, input().strip().split())
graph = []
visit = [[False]*c for _ in range(r)]
for i in range(r):
    graph.append(list(input().strip()))
result = 0

dy = [-1,1,0,0]
dx = [0,0,-1,1]

previous = [0]*26

def dfs(graph, y, x, visited, previous, cur_num):
    global result
    visited[y][x] = True
    result = max(result, cur_num)
    for i in range(4):
        ny, nx = y+dy[i], x+dx[i]
        if ny<0 or ny>=r or nx<0 or nx>=c:
            continue
        if not visited[ny][nx] and previous[ord(graph[ny][nx])-65]==0:
            # previous.append(graph[ny][nx])
            previous[ord(graph[ny][nx])-65] = 1
            # print(ny, nx, graph[ny][nx], previous, cur_num+1)
            dfs(graph, ny, nx, visited, previous, cur_num+1)
    visited[y][x] = False
    previous[ord(graph[y][x])-65] = 0


previous[ord(graph[0][0])-65] = 1
dfs(graph, 0, 0, visit, previous, 1)
print(result)

# if y<0 or y>=r or x<0 or x>=c:
#     return False
# if not visited[y][x] and graph[y][x] not in previous:
#     previous.append(graph[y][x])
#     print(y, x, graph[y][x], previous)
#     dfs(graph, y+1, x, visited, previous, cur_num + 1)
#     dfs(graph, y-1, x, visited, previous, cur_num + 1)
#     dfs(graph, y, x+1, visited, previous, cur_num + 1)
#     dfs(graph, y, x-1, visited, previous, cur_num + 1)
# return True