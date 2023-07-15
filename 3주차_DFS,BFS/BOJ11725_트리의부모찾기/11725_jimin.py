import sys
sys.setrecursionlimit(10**6)

n = int(input())

graph = [[] for _ in range(n+1)]
for _ in range(n-1):
    v1, v2 = map(int,input().split())
    graph[v1].append(v2)
    graph[v2].append(v1)

visited = [False] * (n+1)

answer = [0] * (n+1)

def dfs(v):
    visited[v] = True

    for next_v in graph[v]:
        if not visited[next_v]:
            answer[next_v] = v
            dfs(next_v)

dfs(1)

for i in range(2,n+1): print(answer[i])
