# ----------------------------------------------------
# 1. 처음에는 주어진 주사위의 바닥에 위치한 면이 몇번 면인지 dice_bottom 변수를 하나 두고, dice_bottom 이 1일때 동/서/남/북 으로 이동하는 경우 dice_bottom 은 무슨 수로 변하고...
#    => 요런식으로 풀려 함.
#    => ex. 문제에서 주어진 상태대로 dict_bottom 이 6인 경우, 동/서/남/북 으로 이동 시, 각각 dict_bottom 은 3/4/5/2 로 바뀜.
#    => 이 방법의 문제점: dict_bottom 이 6인 경우 항상 위처럼 이동한다는 보장 X. 경우의 수 더 많음.
# 2. 그럼 주사위 굴리는걸 어케 구현하지? 해서 구글링 해봄.
#    => dice[n] : n 번째 면에 어떤 숫자가 적혀있는가 를 뜻함. dice[0]은 윗면, dice[5]는 바닥면을 뜻함.
#    => 주사위의 회전에 따라 dice[n] 에 적힌 수가 어떻게 바뀌는지 계속 갱신해나가며 시뮬레이션 돌리는 방식.
# ----------------------------------------------------
n,m,x,y,k = map(int,input().split())
_map = []
for _ in range(n):
    _map.append(list(map(int,input().split())))
commands = list(map(int,input().split()))

dice = [0,0,0,0,0,0]

def turn(dir):
    if dir == 1: 
        dice[0], dice[2], dice[3], dice[5] = dice[3], dice[0], dice[5], dice[2]
    elif dir == 2:
        dice[0], dice[2], dice[3], dice[5] = dice[2], dice[5], dice[0], dice[3]
    elif dir == 3:
        dice[0], dice[1], dice[4], dice[5] = dice[4], dice[0], dice[5], dice[1]
    else:
        dice[0], dice[1], dice[4], dice[5] = dice[1], dice[5], dice[0], dice[4]

for c in commands:
    if c == 1:                       # 동
        if y + 1 < m: 
            y += 1
            turn(1)
        else: continue
    elif c == 2:                     # 서
        if y - 1 >= 0: 
            y -= 1
            turn(2)
        else: continue
    elif c == 3:                     # 북
        if x - 1 >= 0: 
            x -= 1 
            turn(3)
        else: continue
    else:                            # 남
        if x + 1 < n: 
            x += 1
            turn(4)
        else: continue
    
    if _map[x][y] == 0:
        _map[x][y] = dice[5]
    else:
        dice[5] = _map[x][y]
        _map[x][y] = 0

    print(dice[0])

