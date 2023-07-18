
n, l, r = map(int, input().split())
countries = []

for i in range(n):
    row = list(map(int, input().split()))
    countries.append(row)

x = 0; y = 0
dx = [1, -1, 0, 0]
dy = [0, 0, -1, 1]

global can_move
can_move = True

days = 0

def search(i, j, temp):

    visited[i][j] = True

    for k in range(4):
        nx = i;
        ny = j
        nx += dx[k]
        ny += dy[k]

        if nx >= n or nx < 0 or ny >= n or ny < 0:
            continue

        if visited[nx][ny]:
            continue

        if l <= abs(countries[i][j] - countries[nx][ny]) <= r:

            temp.append((nx, ny))
            search(nx, ny, temp)


def move(united__):
    sum = 0

    for (i, j) in united__:
        sum += countries[i][j]

    avg = sum // len(united__)

    for (i, j) in united__:
        countries[i][j] = avg


while can_move:
    can_move = False
    visited = [[False] * n for _ in range(n)]
    united = []

    for i, row in enumerate(countries):
        for j, num_people in enumerate(row):
            if visited[i][j]:
                continue

            temp = []
            search(i, j, temp)

            if temp:
                can_move = True
                temp.append((i, j))
                united.append(temp)
                move(temp)

    if can_move:
        days += 1

print(days)


