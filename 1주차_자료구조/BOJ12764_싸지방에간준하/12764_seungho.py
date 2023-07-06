import heapq

n = int(input())
people = []
for _ in range(n):
    heapq.heappush(people, tuple(map(int, input().split())))
# idx = 1
# seats = []
# end_times = []
# available_seats = []
# answers = [0] * 100001

# while people:
#     cur_start, cur_end = heapq.heappop(people)
#     heapq.heappush(end_times, tuple(cur_end, idx))
#     idx += 1
#
#     min_endTime, min_idx = heapq.heappop(end_times)
#     if cur_start < min_endTime:
#         if available_seats: #이용 가능한 좌석이 있다면
#             # 이용 가능 좌석 큐들 중 최소값을 반환 -> 사용처리 후 +1
#             seat_num = heapq.heappop(available_seats)
#             seats[seat_num] = True
#             answers[seat_num] += 1
#         else:
#             #이용 가능한 좌석이 없다면 새 좌석 추가 및 +1
#             seats.append(True)
#             answers[len(seats)] += 1
#     else:
#         heapq.heappush(available_seats)
'''
1st Try : 실패
힙큐를 두개 잡아서 풀려고 했다. (좌석 인덱스 큐 + 최소시작시간 큐)
허나 좌석번호를 인덱싱하여 푸시하려는 과정에서 일일이 인덱스 값을 알수 없어 포기
'''

seats = [0 for _ in range(n)]
seats_count = [0 for _ in range(n)]
seats_num = 0

while people:
    current = heapq.heappop(people)
    for i in range(n):
        if seats[i] <= current[0]:
            if seats[i] == 0:
                seats_num += 1
            seats[i] = current[1]
            seats_count[i] += 1
            break

print(seats_num)
for i in seats_count:
    if i>0:
        print(i, end=" ")
