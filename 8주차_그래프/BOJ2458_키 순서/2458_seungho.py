import sys
import heapq
input = sys.stdin.readline
INF = int(1e9)

n, m = map(int, input().split())
graph=[[False]*(n+1) for _ in range(n+1)]

for i in range(m):
    a, b = map(int, input().strip().split())
    graph[a][b] = True

for k in range(1, n+1):
    for i in range(1, n+1):
        for j in range(1, n+1):
            if graph[i][j]: continue
            if graph[i][k]==True and graph[k][j]==True:
                graph[i][j] = True

answer = 0
for i in range(1,n+1):
    temp = 0
    for j in range(1,n+1):
        temp += graph[i][j] + graph[j][i] #i->j 경우와 j->i 경우를 다 합쳤을 때 n-1개가 나와야 다른 친구들과의 비교관계가 형성되었다는 뜻
    if temp == (n-1):
        answer += 1
print(answer)