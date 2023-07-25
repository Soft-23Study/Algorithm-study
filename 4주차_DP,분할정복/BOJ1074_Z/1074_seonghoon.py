import math

n, r, c = map(int, input().split())

# 몇 사분면인지 계산하는 함수
def calculateQuadrant(i, j, divisor):

    quadrant = 0
    if i/divisor >= 1:
        if j/divisor >= 1:
            quadrant = 4
        else:
            quadrant = 3
    else:
        if j/divisor >= 1:
            quadrant = 2
        else:
            quadrant = 1

    return quadrant

# 몇 사분면에 위치하느냐에 따라 방문 순서가 몇번째부터 시작하는지 계산하는 함수
def calculateOrder(quadrant, n):
    row_size = math.pow(2, n)
    order = row_size * row_size * (quadrant - 1) // 4
    return order

answer = 0
for k in range(n):
    divisor = math.pow(2, n-1)
    quadrant = calculateQuadrant(r, c, divisor)
    answer += calculateOrder(quadrant, n)

    r = r % divisor
    c = c % divisor

    n = n - 1

print(int(answer))