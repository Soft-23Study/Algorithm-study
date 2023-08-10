import heapq

n = int(input())
nums = []
for _ in range(n):
    nums.append(int(input()))

neg = []
pos = []
one = []
zero = []
for num in nums:
    if num == 0: zero.append(0)
    elif num == 1: one.append(1)
    elif num > 0: heapq.heappush(pos,-num)
    else: heapq.heappush(neg,num)

answer = 0

while pos:
    if len(pos) >= 2:
        answer += heapq.heappop(pos) * heapq.heappop(pos)
    else:
        answer += (-1) * heapq.heappop(pos)

while neg:
    if len(neg) >= 2:
        answer += heapq.heappop(neg) * heapq.heappop(neg)
    else:
        if zero:
            zero.pop()
            heapq.heappop(neg)
        else:
            answer += heapq.heappop(neg)

answer += len(one)

print(answer)

