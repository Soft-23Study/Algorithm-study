# 구슬 탈출2
# bfs
# 이게먼...문제..가..

from collections import deque
import sys

input = sys.stdin.readline

n, m = map(int, input().split())
red = [0, 0]
blue = [0, 0]
hole = [0, 0]

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

board = [[0 for _ in range(m)] for _ in range(n)]
for i in range(n):
    tmp = list(input())
    for j in range(m):
        board[i][j] = tmp[j]
        if tmp[j] == 'R':
            red = [i, j]
            board[i][j] = "."
        elif tmp[j] == 'B':
            blue = [i, j]
            board[i][j] = "."
        elif tmp[j] == 'O':
            hole = [i, j]


def move(r, b, direction):
    global hole, board

    red = r[0] * direction[0] + r[1] * direction[1]
    blue = b[0] * direction[0] + b[1] * direction[1]
    marbles = []
    is_finished = [False, False]

    if red >= blue:
        marbles.append(r)
        marbles.append(b)
    else:
        marbles.append(b)
        marbles.append(r)

    while True:
        for i in range(2):
            if is_finished[i]:
                continue
            tr = [marbles[i][0] + direction[0], marbles[i][1] + direction[1]]
            if tr == hole:
                marbles[i] = [-1, -1]
                is_finished[i] = True
            elif board[tr[0]][tr[1]] == "#" or tr == marbles[1 - i]:
                is_finished[i] = True
            else:
                marbles[i] = [tr[0], tr[1]]
        if is_finished[0] and is_finished[1]:
            break

    if red >= blue:
        return marbles
    else:
        return [marbles[1], marbles[0]]


def bfs():
    global n, m, board, red, blue, dx, dy

    queue = deque([[red, blue, 0]])

    while queue:
        red, blue, n = queue.popleft()
        if n >= 10:
            continue

        # 4방향으로 이동
        for i in range(4):
            nr, nb = move(red, blue, [dx[i], dy[i]])
            if red == nr and blue == nb:
                continue
            if nb[0] == -1:
                continue
            elif nr[0] == -1:
                return n + 1
            else:
                queue.append([nr, nb, n + 1])

    return -1

print(bfs())
