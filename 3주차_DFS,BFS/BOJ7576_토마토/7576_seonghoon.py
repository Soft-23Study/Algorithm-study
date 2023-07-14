# 왜 데스크탑으로만 하면 argument가 초과했다고 에러가 날까??
# 그리고 testcase는 전부 통과하는데 실패가 뜨네요 반례를 모르겠어요

from collections import deque

dx = [1, -1, 0, 0] # 동 서 남 북
dy = [0, 0, -1, 1] # 동 서 남 북

m, n = map(int, input().strip().split())
box = []
queue = deque()
day = 0

# 좌표를 위한 x, y 초기화
y = 0
for _ in range(n):
    x = 0
    row = list(map(int, input().rstrip().split()))
    box.append(row)

    for i in row:
        if i == 1:
            queue.append((x, y))
        x += 1

    y += 1

isAlreadyFull = True
# 모든 토마토가 익어있는 상태면 answer = 0
for row in box:
    if 0 in row:
        isAlreadyFull = False

if isAlreadyFull:
    print(0)
    exit(0)

while queue:
    x, y = queue.popleft()

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if nx >= m or nx < 0 or ny >= n or ny < 0:
            continue

        if box[ny][nx] == 0:
            box[ny][nx] = box[ny-dy[i]][nx-dx[i]] + 1
            day = box[ny][nx]
            queue.append((nx, ny))

# 토마토가 모두 익지는 못하는 상황이면 -1 출력
for row in box:
    if 0 in row:
        print(-1)
        exit(0)

day -= 1
print(day)