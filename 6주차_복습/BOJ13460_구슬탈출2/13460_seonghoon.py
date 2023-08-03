# 굉장히 접근하기 어려웠던 문제이다..
# 4차원 배열을 사용하여 해결할 줄도 몰랐다. 결국 답안을 봤음..
# https://hongcoding.tistory.com/125

from collections import deque

n, m = map(int, input().split())
board = []
for _ in range(n):
    row = list(input())
    board.append(row)

visited = [[[[False] * m for _ in range(n)] for _ in range(m)] for _ in range(n)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

for i in range(n): # RED와 BLUE의 위치찾기
    for j in range(m):
        if board[i][j] == 'R':
            ra = i
            rb = j
        elif board[i][j] == 'B':
            ba = i
            bb = j


def roll(x, y, i):
    cnt = 0

    while board[x+dx[i]][y+dy[i]] != '#' and board[x][y] != 'O':
        x += dx[i]
        y += dy[i]
        cnt += 1 # 이 값을 통해 겹쳤을 경우, RED가 앞이었는지 BLUE가 앞이었는지 판단할 것임.

    return x, y, cnt

def bfs():
    queue = deque()
    queue.append((ra, rb, ba, bb, 1))

    while queue:
        rx, ry, bx, by, cnt = queue.popleft()
        visited[rx][ry][bx][by] = True

        if cnt > 10:
            return -1

        for i in range(4):
            nrx, nry, rcnt = roll(rx, ry, i)
            nbx, nby, bcnt = roll(bx, by, i)

            if board[nbx][nby] != 'O':
                if board[nrx][nry] == 'O':
                    return cnt

                if nrx == nbx and nry == nby:
                    if rcnt > bcnt: # rcnt가 크다는 것은 RED가 더 많이 이동했으므로 뒤에 있었다는 뜻이다.
                        nrx -= dx[i]
                        nry -= dy[i]
                    else:
                        nbx -= dx[i]
                        nby -= dy[i]

                if not visited[nrx][nry][nbx][nby]:
                    visited[nrx][nry][nbx][nby] = True
                    queue.append((nrx,nry,nbx,nby, cnt+1))

    return -1

print(bfs())