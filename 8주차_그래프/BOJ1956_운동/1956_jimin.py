INF = int(1e9)

v,e = map(int,input().split())

graph = [[INF] * (v+1) for _ in range(v+1)]
for i in range(1,v+1):
    for j in range(1,v+1):
        if i == j: graph[i][j] = 0

for _ in range(e):
    v1,v2,cost = map(int,input().split())
    graph[v1][v2] = cost

for k in range(1,v+1):
    for i in range(1,v+1):
        for j in range(1,v+1):
            graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])

answer = INF
for i in range(1,v+1):
    for j in range(1,v+1):
        if graph[i][j] + graph[j][i] > 0:
            answer = min(answer, graph[i][j]+graph[j][i])

if answer == INF: print(-1)
else: print(answer)