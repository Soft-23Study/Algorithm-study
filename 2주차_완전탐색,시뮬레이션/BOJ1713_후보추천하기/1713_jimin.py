# ---------------------------------------------------- 1트 => 제출 시 4% 에서 틀림. 왠지모르겠
# 1. '기존에 사진틀에 존재하는 학생인 경우' 에 pic 힙에 pic[i] 인덱싱으로 접근하는게 좀 이상하긴 한데.. 안될 이유는 뭐?
#   => 일단 2트에서 이부분 바꿨더니 통과하긴 함
# ----------------------------------------------------
import heapq

n = int(input())
total = int(input())
students = list(map(int,input().split()))

pic = []

for idx, student in enumerate(students):
    new_flag = True
    # 기존에 사진틀에 존재하는 학생이면
    for i in range(len(pic)):
        if pic[i][2] == student:
            new_flag = False
            pic[i][0] += 1
            break
    # 새로 게시해야 하는 경우라면
    if new_flag:
        if len(pic) == n:
            heapq.heappop(pic)
        heapq.heappush(pic,[1,idx,student])

answer = []
while pic:
    rec,idx,student = heapq.heappop(pic)
    answer.append(student)

answer.sort()
for i in range(len(answer)):
    print(answer[i], end = " ")

# ---------------------------------------------------- 2트
import heapq

n = int(input())
total = int(input())
students = list(map(int,input().split()))

pic = []

for idx, student in enumerate(students):
    temp_heap = []
    new_flag = True
    # 기존에 사진틀에 존재하는 학생이면 추천수 늘려주기
    while pic:
        rec, i, stu = heapq.heappop(pic)
        if stu == student:
            rec += 1
            new_flag = False
        heapq.heappush(temp_heap,(rec,i,stu))
    # 새로 게시해야 하는 경우라면
    if new_flag:
        if len(temp_heap) >= n:
            heapq.heappop(temp_heap)
        heapq.heappush(temp_heap, (0,idx,student))

    pic = temp_heap

answer = []
while pic:
    rec,idx,student = heapq.heappop(pic)
    answer.append(student)

answer.sort()
for i in range(len(answer)):
    print(answer[i], end = " ")