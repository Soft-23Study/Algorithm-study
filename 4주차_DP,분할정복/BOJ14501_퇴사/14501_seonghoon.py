# 풀릴듯 말듯 하다가 막혀서 찾아봄.. 여러 솔루션을 봤지만 이 방식이 내 사고의 흐름과 가장 비슷한 풀이
# 역순으로 살펴보면 knapsack problem과 방식이 유사하다.
# 참고 : https://jewoo-dev.tistory.com/5

import sys

input = sys.stdin.readline

n = int(input().strip())

# n일차 : t[n], p[n]
t = [0] * (n+1)
p = [0] * (n+1)

for i in range(1, n+1):
    t[i], p[i] = map(int, input().strip().split())

# indexError를 방지하기 위해서 n+2까지 만듬
max_p = [0] * (n+2)

# 역순으로 (n일차부터 1일차까지) 탐색함
for i in range(n, 0, -1):
    if i + t[i] > n+1: # if 퇴사하는 날까지 상담을 완료하지 못할 경우
        max_p[i] = max_p[i+1]
    else:
        # i일차에 상담을 하지 않을 경우 -> i+1일차에서의 최대이익
        # i일차에 상담을 할 경우 -> i일차의 이익 + i+t[i]일차의 최대이익
        max_p[i] = max(max_p[i+1], max_p[i + t[i]] + p[i])\

print(max_p[1])