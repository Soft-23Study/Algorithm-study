# 자력으로 풀지 못해서 https://jjunsu.tistory.com/159 를 참고하였다..
# 이분탐색 문제

n, m = map(int, input().split())
jewels = []
for _ in range(m):
    jewels.append(int(input()))
left = 1
right = max(jewels)
min__ = 1_000_000_000

while left <= right:
    mid = (left + right) // 2
    sum = 0
    for i in jewels:
        sum += i // mid
        if (i % mid) > 0:
            sum += 1

    if sum <= n:
        right = mid - 1
        min__ = min(min__, mid)
    else:
        left = mid + 1

print(min__)