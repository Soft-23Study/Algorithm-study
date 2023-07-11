#주사위 굴리기

# <-문제->
# N x M 인 지도 존재
# 지도 좌표 (r,c) 

# 지도 이동한 칸 쓰여있는 수 = 0 -> 바닥면 칸 복사
# 0이 아니면 칸에 쓰여있는 수가 바닥면으로 복사됨 칸 = 0
#동서남북 순

dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]


n, m, x, y, k = map(int, input().split()) # 세로 가로 좌표x,y 명령개수 순
dice = [0,0,0,0,0,0]

def move_go(go):
    if go == 0:
        dice[0], dice[2], dice[3], dice[5] = dice[3], dice[0], dice[5], dice[2]
    elif go == 1:
        dice[0], dice[2], dice[3], dice[5] = dice[2], dice[5], dice[0], dice[3]
    elif go == 2:
        dice[0], dice[1], dice[4], dice[5] = dice[4], dice[0], dice[5], dice[1]
    elif go == 3:
        dice[0], dice[1], dice[4], dice[5] = dice[1], dice[5], dice[0], dice[4]

set=[]
for _ in range(n):
    set.append(list(map(int, input().split())))

move = list(map(int, input().split()))


for i in range(k):
    go = move[i] - 1
    nx = x + dx[go]
    ny = y + dy[go]

    if nx < 0 or nx >= n or ny < 0 or ny >= m:
        continue
    
    move_go(go)

    if set[nx][ny] == 0:
        set[nx][ny] = dice[-1]
    else:
        dice[-1] = set[nx][ny]
        set[nx][ny] = 0

    x, y = nx, ny
    print(dice[0])
