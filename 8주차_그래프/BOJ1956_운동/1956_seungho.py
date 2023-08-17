# 1st: 플로이드로 푸니까 시간초과. (pypy는 가능)
import sys

input = sys.stdin.readline
INF = int(1e9)

v, e = map(int, input().split())
graph = [[INF]*(v+1) for _ in range(v+1)]

for i in range(e):
    start, end, w = map(int, input().strip().split())
    graph[start][end] = w

for k in range(1, v+1):
    for i in range(1, v+1):
        for j in range(1, v+1):
            graph[i][j] = min(graph[i][j], graph[i][k]+graph[k][j])

answer = INF
for i in range(1, v+1):
    answer = min(answer, graph[i][i])

if answer == INF: print(-1)
else: print(answer)
