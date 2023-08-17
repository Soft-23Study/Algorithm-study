# 시간초과 안나는 이유가 뭐지??? 시간복잡도 n^3 -> 워스트 125000000 인데..?

INF = int(1e9)

n,m = map(int,input().split())

graph = [[INF] * (n+1) for _ in range(n+1)]
for i in range(1,n+1):
    for j in range(1,n+1):
        if i == j: graph[i][j] = 0

for _ in range(m):
    v1,v2 = map(int,input().split())
    graph[v1][v2] = 1

for k in range(1,n+1):
    for v1 in range(1,n+1):
        for v2 in range(1,n+1):
            graph[v1][v2] = min(graph[v1][v2], graph[v1][k]+graph[k][v2])

answer = 0
for v1 in range(1,n+1):
    flag = True
    for v2 in range(1,n+1):
        if graph[v1][v2] + graph[v2][v1] == 2 * INF: flag = False
    if flag == True: answer += 1

print(answer)