# 양수, 음수, 0, 1에 대해서 변수를 나누어 관리한다.
# 양수에 대해서는 내림차순, 음수에 대해서는 오름차순으로 정렬후 처리

from heapq import *

n = int(input())

answer = 0

positives = []
negatives = []
num_zeros = 0
num_ones = 0

for _ in range(n):
    num = int(input())
    if num > 1:
        heappush(positives, (-num, num))
    elif num < 0:
        heappush(negatives, num)
    elif num == 1:
        num_ones += 1
    else:
        num_zeros += 1

for _ in range(len(positives)//2):
    answer += heappop(positives)[1] * heappop(positives)[1]

if positives:
    answer += heappop(positives)[1]

for _ in range(len(negatives)//2):
    answer += heappop(negatives) * heappop(negatives)

if negatives:
    if num_zeros > 0:
        num_zeros -= 1 # heappop(negative)를 했다고 치자.
    else:
        answer += heappop(negatives)

for _ in range(num_ones):
    answer += 1

print(answer)