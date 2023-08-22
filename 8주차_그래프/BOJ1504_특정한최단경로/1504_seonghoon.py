# 중요 포인트 : 한번 이동했던 정점, 간선도 다시 이동할 수 있다.
# 2시간동안이나 고민해봤다..
# 답은 뽑히지만 메모리 초과..
# 이후에 다시 살펴보겠다.... + 심지어 경로가 없을때 -1을 출력하지도 않음
import heapq
import sys

INF = sys.maxsize

num_nodes, num_edges = map(int, input().split())

graph = [[INF for _ in range(num_nodes+1)] for _ in range(num_nodes+1)]
total_cost = [INF for _ in range(num_nodes+1)]

for _ in range(num_edges):
    v1, v2, cost = map(int, input().split())
    graph[v1][v2] = graph[v2][v1] = cost

for i in range(1, num_nodes+1):
    total_cost[i] = graph[1][i]

ess1, ess2 = map(int, input().split())

heap = []  # [cost, node 번호, ess1 방문 여부, ess2 방문 여부]

for i in range(2, num_nodes+1):
    if graph[1][i] != INF:
        if i == ess1:
            heapq.heappush(heap, [graph[1][i], i, True, False])
        elif i == ess2:
            heapq.heappush(heap, [graph[1][i], i, False, True])
        else:
            heapq.heappush(heap, [graph[1][i], i, False, False])

while heap:
    cost, node, ess1_visited, ess2_visited = heapq.heappop(heap)

    if node == num_nodes:
        if ess1_visited == True and ess2_visited == True:
            print(cost)
            exit(0)

    for i in range(1, num_nodes+1):
        if graph[node][i] != INF:

            if ess1_visited == True and ess2_visited == True:
                    heapq.heappush(heap, [cost + graph[node][i], i, ess1_visited, ess2_visited])
            else:
                if i == ess1:
                    heapq.heappush(heap, [cost + graph[node][i], i, True, ess2_visited])
                elif i == ess2:
                    heapq.heappush(heap, [cost + graph[node][i], i, ess1_visited, True])
                else:
                    heapq.heappush(heap, [cost + graph[node][i], i, ess1_visited, ess2_visited])

# 1 -> v1 -> v2 -> end 와 1 -> v2 -> v1 -> end 의 각각 최솟값을 봤지만
# 이 방법도 아님
# import heapq
# import sys
#
# INF = sys.maxsize
#
# num_nodes, num_edges = map(int, input().split())
#
# graph = [[INF for _ in range(num_nodes+1)] for _ in range(num_nodes+1)]
#
#
# def dijkstra(start, end):
#     total_cost = [INF for _ in range(num_nodes + 1)]
#
#     for i in range(num_nodes + 1):
#         total_cost[i] = graph[start][i]
#
#     heap = [(0, start)]
#
#     while heap:
#         cost, node = heapq.heappop(heap)
#
#         if total_cost[node] < cost:
#             continue
#
#         for i in range(num_nodes + 1):
#             if cost + graph[node][i] < total_cost[i]:
#                 total_cost = cost + graph[node][i]
#
#     return total_cost[end]
#
#
# for _ in range(num_edges):
#     v1, v2, cost = map(int, input().split())
#     graph[v1][v2] = graph[v2][v1] = cost
#
# ess1, ess2 = map(int, input().split())
#
# answer = min(dijkstra(1,ess1) + dijkstra(ess1,ess2) + dijkstra(ess2,num_nodes), dijkstra(1,ess2) + dijkstra(ess2,ess1) + dijkstra(ess1,num_nodes))
# print(answer)
