# 운동

# 도로 길이 최소 합 다 구해서 비교해야하는 것 같아서 플로이드워셜로 접근 시작
# 3제곱이다보니 python 시간초과 pypy => 성공 (다익스트라 방법으로는 시간 초과 없이 가능할지 시간 날 때 다시 해보기)

import sys
input = sys.stdin.readline

v, e = map(int, input().split())

INF = int(1e9) 
graph = [[INF]*(v+1) for _ in range(v+1)]
answer = int(1e9) 

for _ in range(e):
    a, b, c = map(int, input().split())
    graph[a][b] = c

for k in range(1, v+1): 
	for a in range(1, v+1):
          for b in range(1, v+1):
               if graph[a][k] + graph[k][b] < graph[a][b]:
                    graph[a][b] = min(graph[a][b], graph[a][k]+graph[k][b])
for i in range(1, v+1):
    for j in range(1, v+1):
        if graph[i][j]==INF: print("INF", end=' ')
        else: print(graph[i][j], end=' ')
    print()
for i in range(1, v+1):
    answer = min(answer, graph[i][i])

if answer == 1e9:
    print(-1)
else:
    print(answer)
