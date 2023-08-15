import heapq

n = int(input())
lectures = []
lecture_rooms = []

for _ in range(n):
    lectures.append(list(map(int, input().split())))

lectures.sort()

heapq.heappush(lecture_rooms, lectures[0][1])
for i in range(1, n):
    end_time_of_lecture = heapq.heappop(lecture_rooms)
    if lectures[i][0] < end_time_of_lecture: # 가장 빨리 끝나는 강의보다 빨리 시작하는 강의일 경우,강의실을 새로 만든다
        heapq.heappush(lecture_rooms, end_time_of_lecture)
        heapq.heappush(lecture_rooms, lectures[i][1])
    else: # 가장 빨리 끝나는 강의가 끝난 후에 시작하는 강의일 경우, 그 강의실을 이어서 쓴다.
        heapq.heappush(lecture_rooms, lectures[i][1])

print(len(lecture_rooms))