# 시간초과... 시간을 줄일 수 있는 방법이 떠오르지 않는다

import heapq

people_count = int(input())

heap = []
computers = [[0, 0]] # [count, endTime]


for i in range(0, people_count):
    start_time, end_time = map(int, (input().split()))
    heapq.heappush(heap, (start_time, end_time))

while heap:
    isFull = True
    my_start_time, my_end_time = heapq.heappop(heap)
    for computer in computers: # [count, end_time]
        if my_start_time > computer[1]:
            isFull = False
            computer[0] += 1
            computer[1] = my_end_time
            break
    if isFull:
        computers.append([1, my_end_time])

print(len(computers))
for computer in computers:
    print(computer[0], end=" ")