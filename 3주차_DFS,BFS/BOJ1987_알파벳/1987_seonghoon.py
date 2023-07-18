# 처음에 deque으로 시도하다가 시간 초과가 났고, 해결 방법이 도무지 떠오르지 않아 블로그 포스팅을 봤다..
# 포스팅을 보니 queue가 아닌 set을 사용했는데, 이러면 탐색방법이 bfs는 아니지 않나..?

r, c = map(int, input().split())

board = []
for _ in range(r):
    board.append(list(input()))

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

max_count = 1

queue = set([(0, 0, board[0][0])])

while queue:
    x, y, alpabets = queue.pop()
    max_count = max(max_count, len(alpabets))

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if 0 <= nx < r and 0 <= ny < c and board[nx][ny] not in alpabets:
            queue.add((nx, ny, alpabets + board[nx][ny]))

print(max_count)
