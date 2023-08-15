# 통나무 건너뛰기

import sys
input = sys.stdin.readline

t = int(input())

for _ in range(t):
    n = int(input())
    arr = list(map(int,input().strip().split()))
    arr.sort()

    answer = 0
    # 제일 큰 값 기준으로 양쪽으로 작아지게 
    for i in range(2, n):
        answer = max(answer, abs(arr[i] - arr[i-2]))
    print(answer)
