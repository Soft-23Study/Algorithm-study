# ----------------------------------------------------
# 1. 각 블록 당 가질 수 있는 바닥상태를 block 딕셔너리에 저장
# 2. 주어진 맵의 바닥 상태를 temp 배열에 담아 비교하며 블록을 놓을 수 있는 경우 판별
# ----------------------------------------------------
c,p = map(int,input().split())
_map = list(map(int,input().split()))

block = dict()

block[1] = [[0],[0,0,0,0]]
block[2] = [[0,0]]
block[3] = [[0,0,1],[1,0]]
block[4] = [[1,0,0],[0,1]]
block[5] = [[0,0,0],[0,1],[1,0,1],[1,0]]
block[6] = [[0,0,0],[0,0],[0,1,1],[2,0]]
block[7] = [[0,0,0],[0,0],[1,1,0],[0,2]]

answer = 0
for case in block[p]:
    if len(case) == 1: answer += c
    else:
        for i in range(c-len(case)+1):
            temp = []
            for j in range(len(case)):
                temp.append(_map[i+j]-min(_map[i:i+len(case)]))
            if temp == case:
                answer += 1

print(answer)