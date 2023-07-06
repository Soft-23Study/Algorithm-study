# ---------------------------------------------------- 1트 => 제출 시 10% 에서 틀림
# [ 풀이 방식 ]
# 1. input_q : 입장 순서가 빠른 사람 순으로 뽑아주는 우선순위 큐. (시작시간, 종료시간) 저장
# 2. output_q : 현재 사용 중인 자리번호가 끝나는 시간을 저장하는 우선순위 큐. 끝나는 시간이 빠른 순으로 pop 해줄 수 있다. (끝나는 시간, 자리번호) 저장
# 3. input_q 에서 한명 뽑아왔을 때, 새로운 자리가 필요하다면(else문) -> 새로운 자리에 / 기존에 사용중이던 자리가 빈다면(if문) -> 거기에 넣어주기
# [ 틀리는 케이스 ]
# => 주어진 예제에 (100,150) 인 사람을 추가하면 1번 자리로 가야 하는데, 4번 자리로 보내서 틀리게 됨
# [ 틀리는 이유 ]
# => (100,150) 인 사람이 들어오는 시점에 output_q 에는 (90,4), (100,1), (110,2), (120,3) 순서로 들어있기 때문
# => (90,4) 가 아닌 (100,1) 까지 뽑아야 한다!
# ----------------------------------------------------
# import heapq, sys

# n = int(sys.stdin.readline())

# input_q = []
# output_q = []

# for _ in range(n):
#     start, end = map(int,sys.stdin.readline().split())
#     heapq.heappush(input_q,(start,end))

# seats = [0] * n
# seat_num = 0

# while input_q:
#     (start, end) = heapq.heappop(input_q)

#     if output_q and start >= output_q[0][0]:
#         (poped_end, poped_seat) = heapq.heappop(output_q)
#         heapq.heappush(output_q,(end,poped_seat))
#         seats[poped_seat] += 1
#     else:
#         heapq.heappush(output_q,(end,seat_num))
#         seats[seat_num] += 1
#         seat_num += 1

# answer = 0
# answer_arr = []

# for seat in seats:
#     if seat > 0:
#         answer += 1
#         answer_arr.append(seat)

# print(answer)
# for a in answer_arr: print(a, end=" ")

# ---------------------------------------------------- 2트 => 성공
# [ 주의점 ]
# => heappop 을 하기 전에는 항상 heap 이 비어있진 않은지 확인해주자 (비어있는 힙에서 팝하면 IndexError 발생)
# [ 1트와의 차이점 ]
# 1. avail_seats 힙 추가 : 현재 시점에서 자리 증설 없이 사용 가능한 자리들을 자리번호 낮은 순으로 관리
# ----------------------------------------------------
import heapq, sys

n = int(sys.stdin.readline())

input_q = []
output_q = []
avail_seats = []

for _ in range(n):
    start, end = map(int,sys.stdin.readline().split())
    heapq.heappush(input_q,(start,end))

seats = [0] * n
seat_num = 0

while input_q:
    (start, end) = heapq.heappop(input_q)

    if output_q and start >= output_q[0][0]:
        while start >= output_q[0][0]:
            (poped_end, poped_seat) = heapq.heappop(output_q)
            heapq.heappush(avail_seats,poped_seat)
        next_seat = heapq.heappop(avail_seats)
        heapq.heappush(output_q,(end,next_seat))
        seats[next_seat] += 1
    else:
        if avail_seats:
            next_seat = heapq.heappop(avail_seats)
            heapq.heappush(output_q,(end,next_seat))
            seats[next_seat] += 1
        else:
            heapq.heappush(output_q,(end,seat_num))
            seats[seat_num] += 1
            seat_num += 1

answer = 0
answer_arr = []

for seat in seats:
    if seat > 0:
        answer += 1
        answer_arr.append(seat)

print(answer)
for a in answer_arr: print(a, end=" ")




