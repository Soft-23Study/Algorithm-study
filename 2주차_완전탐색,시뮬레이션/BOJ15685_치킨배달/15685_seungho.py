#시작 시간 : 11:54
import sys
from itertools import combinations
from collections import deque

input = sys.stdin.readline

n, m = map(int, input().strip().split())
city = [[-1]*(n+1) for _ in range(n+1)]

chicken_houses = []
houses = []
for i in range(1, n+1):
    temp = list(map(int, input().strip().split()))
    for j in range(1, n+1):
        city[i][j] = temp[j-1]
        if city[i][j] == 2:
            chicken_houses.append((i,j))
        elif city[i][j] == 1:
            houses.append((i,j))

list_chicken = list(combinations(chicken_houses, m))

dy = [-1,1,0,0]
dx = [0,0,-1,1]

'''
1st Try : BFS로 치킨집의 상하좌우 이동패턴을 추적하여 최소 치킨거리를 구하려고 했다.
하지만 두개의 치킨집이 하나의 집에 대해 더욱 최소값을 갖는 치킨집을 찾는게 난항을 겪다가 접어버렸다.
-> 문제 자체에서 공식을 굳이 주며 치킨거리를 구하는 것을 보고, 수식으로 풀어야겠다고 생각했다.
'''
# for chickens in list_chicken:
#     queue = deque([])
#
#     for chic in chickens:
#         queue.append([chic[0], chic[1], 0]) #[y, x, distance]
#     visited = [[False] * (n + 1) for _ in range(n + 1)]
#     while queue:
#         cur_y, cur_x, cur_dist = queue.popleft()
#         for i in range(4):
#             ny, nx = cur_y + dy[i], cur_x + dx[i]
#             if nx<=0 or nx>n or ny<=0 or ny>n or city[ny][nx]==2:
#                 continue
#             if city[ny][nx] == 1 and not visited[ny][nx]:
#                 visited[ny][nx] = True
#                 queue.append([ny, nx, cur_dist + 1])
#             else:
#                 visited[ny][nx] = True
#                 queue.append([ny, nx, cur_dist + 1])

'''
2nd Try
모든 조합 케이스에 대해 완전탐색.
각 케이스마다의 도시거리를 리스트에 추가한 후 마지막에 최소 도시거리 출력하니까 바로 된다.
'''
minimum_dist = []
for chickens in list_chicken:
    city_chicken_dist = 0
    for house in houses:
        chicken_dist = 2501 #나올수없는값
        for chicken in chickens:
            chicken_dist = min(chicken_dist, abs(chicken[0]-house[0])+abs(chicken[1]-house[1]))
        city_chicken_dist += chicken_dist
    minimum_dist.append(city_chicken_dist)
print(min(minimum_dist))
