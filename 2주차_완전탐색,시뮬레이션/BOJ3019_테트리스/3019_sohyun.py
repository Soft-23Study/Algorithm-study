# 테트리스

# <--문제-->
# 블록 떨어뜨리기 전에 회전 90 180 270 or 좌우 필드 벗어나지 않게
# 블록을 놓는 서로 다른 방법의 수를 구하시오

# import numpy as np

c , p = map(int,input().split()) # 칸 갯수 # 떨어트릴 블록 번호

height = [*map(int,input().split())] # 높이 리스트

# 블럭의 높이 비어있는 부분 체크
block = dict()
block[1] = [[0],[0,0,0,0]] # 모든 경우가 가능
block[2] = [[0,0]]
block[3] = [[0,0,1],[1,0]]
block[4] = [[1,0,0],[0,1]]
block[5] = [[0,0,0],[0,1],[1,0,1],[1,0]]
block[6] = [[0,0,0],[0,0],[0,1,1],[2,0]]
block[7] = [[0,0,0],[0,0],[1,1,0],[0,2]]

# block[p]의 첫번째 요소 부터 확인
# 1st 알고리즘
# block의 여러 경우의 수를 하나씩 대입
# 그 때 사용되는 밑바닥 칸에 맞춰서 테트리스 칸도 같은 값으로 맞춰주면서 계산
# 높이에 대한 정보 - 칸에 대한 정보 행렬 차 = 그 배열의 값이 모두 일치 해야함 -> 그러면 가능한 경우

count = 0
for i in block[p]:
    # print(i)
    start = 0
    fin = len(i)
    while fin<c+1 :
        a = height[start:fin]     
        arr = [a-i for a,i in zip(a,i) ] #배열의 차 계산
        arr = set(arr) # 중복된 값 제거 -> 1개면 모두 같은 값 가진거겠지
        if len(arr) == 1 :
            count+=1
        start+=1
        fin+=1
    

print(count)

