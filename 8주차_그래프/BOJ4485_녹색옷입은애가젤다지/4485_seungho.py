# 다익스트라로 풀되, 인접 그래프로 입력을 받지 못함을 깨닫고 살짝 변형해야겠다고 생각
# 현재 노드와 인접한 노드를 찾을 때 "상하좌우" 패턴을 이용하여 다익스트라 실행

import sys
import heapq
input = sys.stdin.readline

INF = int(1e9)
idx = 1
while True:
    n = int(input())
    if n == 0: break
    cave = []
    for i in range(n):
        cave.append(list(map(int, input().strip().split())))
    q = []
    dist = [[INF]*n for _ in range(n)]
    dist[0][0] = cave[0][0]
    heapq.heappush(q, (dist[0][0], 0, 0))

    while q:
        dist_sofar, cur_y, cur_x = heapq.heappop(q)
        if dist_sofar < dist[cur_y][cur_x]:
            continue
        for vec in [(-1,0),(1,0),(0,-1),(0,1)]:
            ny, nx = cur_y+vec[0], cur_x+vec[1]
            if ny<0 or ny>=n or nx<0 or nx>=n:
                continue
            cost = dist_sofar + cave[ny][nx]
            if dist[ny][nx] > cost:
                dist[ny][nx] = cost
                heapq.heappush(q, (cost, ny, nx))
    print(f'Problem {idx}: {dist[n-1][n-1]}')
    idx += 1