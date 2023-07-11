Map = []
dx = [0, 0, -1, 1]  # 동 서 북 남
dy = [1, -1, 0, 0]  # 동 서 북 남
dice = [0, 0, 0, 0, 0, 0]



def turn(direction):
    a, b, c, d, e, f = dice[0], dice[1], dice[2], dice[3], dice[4], dice[5]
    if direction == 1:
        dice[0], dice[1], dice[2], dice[3], dice[4], dice[5] = e, b, f, d, c, a
    elif direction == 2:
        dice[0], dice[1], dice[2], dice[3], dice[4], dice[5] = f, b, e, d, a, c
    elif direction == 3:
        dice[0], dice[1], dice[2], dice[3], dice[4], dice[5] = b, c, d, a, e, f
    else:
        dice[0], dice[1], dice[2], dice[3], dice[4], dice[5] = d, a, b, c, e, f


n, m, x, y, command = map(int, input().split())

for _ in range(n):
    row = list(map(int, input().split()))
    Map.append(row)

command = list(map(int, input().split()))

for i in command:
    x += dx[i - 1]
    y += dy[i - 1]

    # map을 벗어날 경우 원상복구
    if x < 0 or x >= n or y < 0 or y >= m:
        x -= dx[i - 1]
        y -= dy[i - 1]
        continue

    turn(i)

    if Map[x][y] == 0:
        Map[x][y] = dice[2]
    else:
        dice[2] = Map[x][y]
        Map[x][y] = 0

    print(dice[0])

