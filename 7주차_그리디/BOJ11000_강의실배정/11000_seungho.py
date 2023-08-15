# 1트 : 시간초과 (날줄알고했는데 나네)
# n = int(input())
# times = [[0]*3 for _ in range(n)]
# for i in range(n):
#     times[i][0], times[i][1] = map(int, input().split())
#     times[i][2] = abs(times[i][0]-times[i][1])
# times = sorted(times, key= lambda x: x[2], reverse=True)
# print(times)
# classes = [[times[0]]]
# for i in range(1, len(times)):
#     saved = False
#     for j in range(len(classes)):
#         for k in range(len(classes[j])):
#             if classes[j][k][0]<=times[i][0]<classes[j][k][1] or classes[j][k][0] < times[i][1] <= classes[j][k][1]:
#                 break
#             if k == len(classes[j])-1 and saved == False:
#                 classes[j].append(times[i])
#                 saved = True
#                 break
#         if j == len(classes)-1 and saved == False:
#             classes.append([times[i]])
#             break
# print(classes)

# 2트 : 종료시간을 기준으로 heapq 처리. 강의 사이시간에 해당 타임이 들어가면 어쩌지 하고 넘겨짚었었는데,
# 시작시간으로 정렬한 상태에서 시작하니 그런 예외가 안생긴다는 걸 깨달음.
import sys
import heapq

heap = []
input = sys.stdin.readline

n = int(input())
arr = []
for i in range(n):
    a, b = map(int, input().split())
    arr.append([a, b])
arr.sort()

heapq.heappush(heap, arr[0][1])
for i in range(1, n):
    if heap[0] > arr[i][0]:
        heapq.heappush(heap, arr[i][1])
    else:
        heapq.heappop(heap)
        heapq.heappush(heap, arr[i][1])
print(len(heap))




