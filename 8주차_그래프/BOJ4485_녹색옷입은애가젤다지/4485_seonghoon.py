# 풀다가 머리가 안돌아가서 블로그를 참고했다..
# 정답률 50%짜리 문제인데도 해매는 것 보면 다익스트라에 대한 개념이 부족한 듯

import heapq
import sys

INF = sys.maxsize

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
k = 1 # 시행횟수 출력을 위한 변수

while True:

    n = int(input())
    if n == 0:
        break

    maze = [] # 입력값을 넣을 2차원 배열
    for _ in range(n):
        maze.append(list(map(int, input().split())))

    total_money = [[INF for _ in range(n)] for _ in range(n)] # 최소 비용을 저장할 2차원 배열
    total_money[0][0] = maze[0][0]

    heap = [(maze[0][0], (0, 0))]

    while heap:
        money, cur = heapq.heappop(heap)
        if money < total_money[cur[0]][cur[1]]: # 시간 단축을 위해 작성
            continue

        for i in range(4):
            nx, ny = cur[0] + dx[i], cur[1] + dy[i]
            if 0 <= nx < n and 0 <= ny < n:
                if total_money[cur[0]][cur[1]] + maze[nx][ny] < total_money[nx][ny]:
                    total_money[nx][ny] = total_money[cur[0]][cur[1]] + maze[nx][ny]
                    heapq.heappush(heap, (total_money[nx][ny], (nx, ny)))

    print("Problem {0}: {1}".format(k, total_money[n-1][n-1]))
    k += 1