"""
아직 다 못풀어서, 전반적인 문제 접근법만 우선 기재한 후, 추후 완성하면 푸시하겠습니다.
1. 각 블록의 타입에 맞게 시작 위치로부터 나타날 수 있는 모든 방향에 대해 벡터화 시켰다.
(예: 긴막대기:[[(0,1),(0,2),(0,3)],[(1,0),(2,0),(3,0)]]가 (1,1)부터 시작? -> (1,1),(1,2),(1,3),(1,4) / (1,1),(2,1),(3,1),(4,1))
2. 블록이 배치되었을 때, 기존 블록들과 비교 시 공백이 있는지 없는지
-> 있으면 count +=1, 없으면 continue
"""


import sys

input = sys.stdin.readline

c, p = map(int, input().strip().split())

line = list(map(int, input().strip().split()))


blocks = [[], #번호 편안하게 하기 위한 0번 인덱스 빈칸
          [[(0,1),(0,2),(0,3)],[(1,0),(2,0),(3,0)]], #1번 블록
          [[(1,0),(0,1),(1,1)]], #2번 블록
          [[(1,0),(1,1),(2,1)],[(0,1),(1,0),(1,-1)]], #3번 블록
          [[(1,0),(1,-1),(2,-1)],[(0,1),(1,1),(1,2)]], #4번 블록
          [[(1,0),(2,0),(1,1)],[(1,1),(1,0),(1,-1)],[(1,0),(2,0),(1,-1)],[(0,1),(0,2),(1,1)]],#5번 블록
          [[(1,0),(2,0),(2,1)],[(1,0),(1,-1),(1,-2)],[(0,1),(1,1),(2,1)],[(1,0),(0,1),(0,2)]], #6번 블록
          [[(0,1),(1,0),(2,0)],[(0,1),(0,2),(1,2)],[(1,0),(2,0),(2,-1)],[(1,0),(1,1),(1,2)]]] #7번 블록

cur_block = blocks[p]

for cur_line in range(c):
    #0번째 행부터 c-1번쨰 행까지 완전탐색
    for block_direction in cur_block:
        # block_direction : 블록이 돌려질 수 있는 모든 경우의 수
        cur_block_pos = [[cur_line, line[cur_line]-1]]
        isPass = True
        cur_block_height = [-1]*4
        for vector in block_direction:
            #각 블록의 방향벡터에 대하여
            temp_pos_x, temp_pos_y = cur_block_pos[0][0] + vector[0], cur_block_pos[0][1] + vector[1]
            cur_block_pos.append([temp_pos_x, temp_pos_y])
            if temp_pos_x >= c:
                isPass = False
                break
            if line[temp_pos_x] -1 >= temp_pos_y:
                isPass = False
                break
            if cur_block_height[vector[0]] == -1:
                cur_block_height[vector[0]] = temp_pos_y
            else:
                cur_block_height[vector[0]] = min(cur_block_height[vector[0]], temp_pos_y)
        for h in range(4):
            if cur_block_height[h] == -1:
                isPass = False
                break
            if cur_block_height[h] - line[] > 1

        if not isPass:
            continue



