# ---------------------------------------------------- 답 참고
# 1. 이분탐색 사용 << 이분탐색임 쓰는걸 떠올리기가 어려운 문제
# 2. mid 값을 '한 사람이 가져가는 보석 수' 로 잡고, 그에 따른 사람 수 (peoples) 와 n 값을 비교
# 3. peoples > n 이면, 한 명이 가져가는 보석 수를 늘린다 / peoples < n 이면, 한 명이 가져가는 보석 수를 줄인다
# ----------------------------------------------------
import sys

n,m = map(int,input().split())
jewels = []
for _ in range(m):
    jewels.append(int(sys.stdin.readline()))

jewels.sort(reverse = True)

left = 1
right = max(jewels)

while left <= right:
    mid = (left+right) // 2
    peoples = 0

    for jewel in jewels:
        if jewel % mid == 0:
            peoples += jewel // mid
        else:
            peoples += jewel // mid + 1
        
    if peoples > n:
        left = mid + 1
    else:
        right = mid - 1

print(left)