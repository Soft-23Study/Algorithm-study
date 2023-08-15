# 작은 값 2개씩 순서대로 맨앞, 맨뒤에 처리

import heapq
from collections import deque

t = int(input())

for _ in range(t):
    n = int(input())
    logs = list(map(int, input().split()))
    heapq.heapify(logs)

    arr = [0] * n

    arr[0] = heapq.heappop(logs)
    arr[n-1] = heapq.heappop(logs)
    max_length = arr[n - 1] - arr[0]
    i = 1
    j = n - 2

    while i < j:
        arr[i] = heapq.heappop(logs)
        arr[j] = heapq.heappop(logs)

        if arr[i] - arr[i-1] > max_length:
            max_length = arr[i] - arr[i-1]
        if arr[j] - arr[j+1] > max_length:
            max_length = arr[j] - arr[j+1]

        i += 1
        j -= 1

    # 홀수개일 경우, 반복문이 종료되어 처리되지 않는 숫자 1개가 있는데, 그 부분을 처리
    if logs:
        arr[i] = heapq.heappop(logs)

        if arr[i] - arr[i-1] > max_length:
            max_length = arr[i] - arr[i-1]
        if arr[i] - arr[i+1] > max_length:
            max_length = arr[i] - arr[i+1]

    # 짝수개일 경우, 연산하지 않는과정을 처리
    if abs(arr[i] - arr[j]) > max_length:
        max_length = abs(arr[i] - arr[j])

    print(max_length)
