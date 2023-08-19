# 서강 그라운드

# 플로이드워셜

import sys
INF = int(1e9)
input = sys.stdin.readline
n, m, r = map(int, input().split())
graph = [[INF]*(n+1) for _ in range(n + 1)]

answer = 0
items = [0] + [int(x) for x in input().split()]

for _ in range(r):
    a, b, l = map(int, sys.stdin.readline().split())
    graph[a][b] = l
    graph[b][a] = l

for i in range(n + 1):
    graph[i][i] = 0

for k in range(1, n + 1):
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])

for i in range(1, n + 1):
    tmp = 0
    for j in range(1, n + 1):
        if graph[i][j] <= m:
            tmp += items[j]

    answer = max(answer, tmp)

print(answer)
