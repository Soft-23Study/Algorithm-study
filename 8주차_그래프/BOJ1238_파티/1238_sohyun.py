# 파티

# 다익스트라

import heapq
import sys

input = sys.stdin.readline
INF = int(1e9)
 
n, m, x = map(int, input().split())

graph = [[] for _ in range(1+n)]
graphR = [[] for _ in range(1+n)]
dis = [INF] * (n+1)
dis_change = [INF] * (n+1)
 
for _ in range(m):
  a, b, c = map(int, input().split())
  graph[a].append((b, c))
  graphR[b].append((a, c))
  
def dijkstra(start):
  q = []
  heapq.heappush(q, (0, start))
  dis[start] = 0

  while q:
    dist, now = heapq.heappop(q)

    if dis[now] < dist:
      continue

    for i in graph[now]:
      cost = dist + i[1]
      
      if cost < dis[i[0]]:
        dis[i[0]] = cost
        heapq.heappush(q, (cost, i[0]))
 
def dijkstra_change(start):
  q = []
  heapq.heappush(q, (0, start))
  dis_change[start] = 0
  while q:
    dist, now = heapq.heappop(q)

    if dis_change[now] < dist:
      continue
    
    for i in graphR[now]:
      cost = dist + i[1]

      if cost < dis_change[i[0]]:
        dis_change[i[0]] = cost
        heapq.heappush(q, (cost, i[0]))
        
dijkstra(x)
dijkstra_change(x)
 
result = []
for i in range(1, n+1):
  result.append(dis[i] + dis_change[i])
 
result.sort(reverse = True)
print(result[0])
