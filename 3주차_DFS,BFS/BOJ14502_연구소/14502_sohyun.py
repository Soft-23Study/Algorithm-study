# 뭔가 안되고 있는데 이유를 모르겠는데
# 일단 결과를 12시 전에 올립니다 -> 이후 다시 보고 커밋 예정

# 연구소

# <-문제 ->
# nm 직사각형 연구소 빈칸 / 벽 / 바이러스
# 바이러스 => 상하좌우
# 새로 세울 수 있는 벽 = 3개

# 0 : 빈칸 / 1 : 벽 / 2 : 바이러스
# 바이러스가 퍼질 수 없는 안전 영역 크기 최댓값 ?

# 1st 알고리즘
# 무조건 bfs
# 조합을 쓴다? nm개 중에 3개를 고르고 이안에서
# 최댓값이 되는 조합을 찾는다 ? 

# 그 조합을 기준으로 바이러스 퍼트려서 값을 각각 찾아
# bfs를 하는데 2는 상하좌우로 풀어

# from itertools import combinations  조합을 쓴다면 ?

# 그럼 일단 2인게 어디칸인지 저장해서
# queue에넣고 빌때까지 반복 

import sys
from collections import deque
input = sys.stdin.readline

board = []
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]
queue = deque()
answer=0

def part_check() : 
    part=0
    # print(board)
    while queue:
        x,y = queue.popleft() # 이곳의 2자리를 봅니다
        # print(x,y)
        # print("1.", x,y)

        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]
            # print("2.", nx,ny)
            #영역을 넘어갔을 경우
            if nx<0 or nx>=n or ny<0 or ny>=m: 
                continue
            if board[nx][ny]==0 :
                board[nx][ny]=2 # 바이러스가 전염된 상태
                queue.append((nx,ny)) # 재귀적으로 얘도 전염상태 찾아야지

    # 나온 결과의 0인 영역을 찾는다
    for i in range(n):
            part += board[i].count(0)       

    # print(board)
    # print(part)
    # 그리고 비교한다 -> 영역이랑 기존 최댓값을
    # global answer
    # answer = max(part,answer)
    return part

    
# 조합을 쓰려했는데 간단할 줄 알았는데 오히려 너무나도 복잡해져서 수동으로 돌린다
def random(ca):
    if ca == 3:
        # 랜덤으로 3개 만들고 그거 채운 값으로 구하기
        check = part_check()
        global answer
        answer = max(check,answer) #최댓값 갱신
        return

    for i in range(n):
        for j in range(m):
            if board[i][j] == 0:
                board[i][j] = 1
                random(ca+1)
                board[i][j] = 0

#시작

n,m = map(int,input().strip().split())

for i in range(n):
    board.append(list(map(int, input().split())))

for i in range(n):
        for j in range(m):
            if board[i][j] == 2:
                queue.append((i, j))
        
# print(queue) 2인자리 담고
random(0)
print(answer)



