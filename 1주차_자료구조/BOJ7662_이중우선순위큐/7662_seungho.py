from collections import deque
import sys

input = sys.stdin.readline

tc = int(input().strip())
for _ in range(tc):
    q = []
    k = int(input().strip())

    for i in range(k):
        type, value = input().strip().split()
        value = int(value)
        if type == 'I':
            q.append(value)
        else:
            if len(q) == 0:
                continue
            if value == 1:
                # 최댓값 삭제
                # 최댓값이 둘 이상인 경우 하나만 삭제
                q.remove(max(q))

            else:
                # 최솟값 삭제
                # 최솟값이 둘 이상인 경우 하나만 삭제
                q.remove(min(q))

    if len(q)==0: print("EMPTY")
    else:
        print(max(q), min(q))
