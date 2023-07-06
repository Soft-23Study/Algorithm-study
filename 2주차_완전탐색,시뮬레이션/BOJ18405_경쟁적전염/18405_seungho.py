import sys
from collections import deque

input = sys.stdin.readline

n, k = map(int, input().strip().split())
arr = [[-1]*(n+1) for _ in range(n+1)] #n+1 * n+1 크기의 맵

temp_queue = []
queue = deque([])

for i in range(1, n+1):
    temp = list(map(int, input().strip().split()))
    for j in range(1, n+1):
        arr[i][j] = temp[j-1]
        if temp[j-1] > 0:
            #[바이러스no, y, x, time]
            temp_queue.append([temp[j-1], i, j, 0])

s, x, y = map(int, input().strip().split())

for i in sorted(temp_queue):
    queue.append(i) #초기 바이러스 위치 파악 후 큐에 삽입


dy = [-1,1,0,0] #상, 하, 좌, 우
dx = [0,0,-1,1]

while queue:
    cur_type, cur_y, cur_x, cur_time = queue.popleft()
    for i in range(4):
        ny = cur_y + dy[i]
        nx = cur_x + dx[i]
        if nx<1 or nx>n or ny<1 or ny>n: #벽을 벗어난다면
            continue
        if arr[ny][nx] > 0: #이미 바이러스가 있다면
            continue
        if cur_time==s: #목표 시간이 되었다면
            continue
        if arr[ny][nx] == 0: #바이러스가 없다면
            queue.append([cur_type, ny, nx, cur_time+1]) #큐에 바이러스 삽입
            arr[ny][nx]=cur_type #맵에 바이러스 표시
print(arr[x][y])