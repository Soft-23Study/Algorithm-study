
import heapq
import sys

heap = []

num = int(input())
for i in range(num):
    n = int(sys.stdin.readline().rstrip())
    if n != 0:
        heapq.heappush(heap, (abs(n), n))
    else:
        if not heap:
            print(0)
        else:
            print(heapq.heappop(heap)[1])


# 왜 틀렸다고 할까? 결과는 같은데..?
# import heapq
# import sys
#
# heap = []
#
# num = int(input())
# for i in range(num):
#     n = int(sys.stdin.readline().rstrip())
#
#     if n == 0:
#         if len(heap) != 0:
#             (element, isNegative) = heapq.heappop(heap)
#             if not isNegative:
#                 element = -element
#             print(element)
#         else: print(0)
#     elif n < 0:
#         heapq.heappush(heap, (-n, True))
#     else:
#         heapq.heappush(heap, (n, False))
