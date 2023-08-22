'''
미완성코드입니다. (테스트코드는 정답이나 틀렸습니다 판정)
'''



import sys
input = sys.stdin.readline
import heapq

INF = int(1e9)

n, e = map(int, input().split())
graph = [[] for _ in range(n+1)]

for i in range(e):
    a, b, c = map(int, input().strip().split())
    graph[a].append((c, b))
    graph[b].append((c, a))

dist = [INF]*(n+1)
dist[1] = 0

mid_start, mid_end = map(int, input().split())
mid_cost = 0
for t in graph[mid_start]:
    if t[1] == mid_end:
        mid_cost = t[0]
        break

def dijkstra(graph, dist, start, goal):
    q = []
    heapq.heappush(q, (dist[start], start))
    while q:
        dist_sofar, now = heapq.heappop(q)
        if dist_sofar > dist[now]:
            continue
        for n in graph[now]:
            cost = dist_sofar + n[0]
            if cost < dist[n[1]]:
                dist[n[1]] = cost
                heapq.heappush(q, (cost, n[1]))
    return dist[goal]
result1 = dijkstra(graph, dist, 1, mid_start) + mid_cost
dist = [INF]*(n+1)
dist[mid_end]=0
result1 += dijkstra(graph, dist, mid_end, n)

result2 = dijkstra(graph, dist, 1, mid_end) + mid_cost
dist = [INF]*(n+1)
dist[mid_start]=0
result2 += dijkstra(graph, dist, mid_start, n)
print(min(result1, result2))
