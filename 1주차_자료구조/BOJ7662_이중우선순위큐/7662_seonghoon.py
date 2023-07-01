# 두 번 풀어봤으나 계속 시간초과가 발생하여 풀이를 찾아봄
import heapq


test_count = int(input())

for i in range(test_count):
    input_count = int(input())
    min_heap = []
    max_heap = []
    visited = [False] * 100_0000

    for j in range(input_count):
        op, n = input().split()
        n = int(n)

        if op == "I":
            heapq.heappush(min_heap, (n, j))
            heapq.heappush(max_heap, (-n, j))
            visited[j] = True
        elif op == "D":
            if n == 1:
                while max_heap and not visited[max_heap[0][1]]: heapq.heappop(max_heap)
                if max_heap:
                    index = heapq.heappop(max_heap)[1]
                    visited[index] = False
            else:
                while min_heap and not visited[min_heap[0][1]]: heapq.heappop(min_heap)
                if min_heap:
                    index = heapq.heappop(min_heap)[1]
                    visited[index] = False

    while max_heap and not visited[max_heap[0][1]]: heapq.heappop(max_heap)
    while min_heap and not visited[min_heap[0][1]]: heapq.heappop(min_heap)

    # 출력
    if not max_heap:
        print("EMPTY")
    else:
        print("{0} {1}".format(-max_heap[0][0], min_heap[0][0]))


# deque으로 할 경우 시간초과

# from collections import deque
#
# test_count = int(input())
#
# for i in range(test_count):
#     input_count = int(input())
#     queue = deque()
#
#     for j in range(input_count):
#         op, n = input().split()
#         n = int(n)
#
#         if op == "I":
#             queue.append(n)
#         elif op == "D" and queue:
#             if n == 1:
#                 queue.remove(max(queue))
#             else:
#                 queue.remove(min(queue))
#
#     # 출력
#     if not queue:
#         print("EMPTY")
#     else:
#         print("{0} {1}".format(max(queue), min(queue)))

# 이 또한 시간초과

# import heapq
#
# test_count = int(input())
#
# for i in range(test_count):
#     input_count = int(input())
#     queue = []
#
#     for j in range(input_count):
#         op, n = input().split()
#         n = int(n)
#
#         if op == "I":
#             heapq.heappush(queue, n)
#         elif op == "D" and queue:
#             if n == 1:
#                 queue.remove(heapq.nlargest(1, queue)[0])
#             else:
#                 heapq.heappop(queue)
#
#     # 출력
#     if not queue:
#         print("EMPTY")
#     else:
#         print("{0} {1}".format(heapq.nlargest(1, queue)[0], heapq.nsmallest(1, queue)[0]))

