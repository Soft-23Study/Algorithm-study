# 개인적으로 어려웠다. 이분탐색으로 이렇게 풀수 있다는걸 배웠다.

k, n = map(int, input().split())

min_length = 1
max_length = 0
lines = []
answer = 0
for _ in range(k):
    length = int(input())
    lines.append(length)
    max_length = max(max_length, length)

while min_length <= max_length:
    mid_length = (max_length + min_length) // 2

    num = 0
    for i in range(k):
        num += lines[i] // mid_length

    if num >= n:
        min_length = mid_length + 1
        answer = max(answer, mid_length)
    else:
        max_length = mid_length - 1


print(answer)