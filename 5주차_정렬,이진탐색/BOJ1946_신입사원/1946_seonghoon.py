test_num = int(input())

for _ in range(test_num):
    n = int(input())

    grade = [[0 for i in range(2)] for j in range(n)]

    answer = 1

    for i in range(n):
        grade[i][0], grade[i][1] = map(int, input().split())

    grade.sort(key=lambda x:x[0])

    person_of_most_interview_grade = grade[0][1]
    for i in range(1, n):
        can_employed = True
        if grade[i][1] < person_of_most_interview_grade:
            person_of_most_interview_grade = grade[i][1]
            answer += 1

    print(answer)

# 지원서에서 내가 순위가 낮은 경우를 추리고,
# 그 목록에서만 내 면접 순위가 낮은 경우를 추리는데도 시간 초과..

# test_num = int(input())
#
# for _ in range(test_num):
#     n = int(input())
#
#     applications = []
#     interviews = []
#     answer = 0
#
#     for _ in range(n):
#         application, interview = map(int, input().split())
#         applications.append(application)
#         interviews.append(interview)
#
#     for i in range(n):
#         temps = []
#         can_employed = True
#
#         for j in range(n):
#             if i == j: continue
#
#             if applications[i] > applications[j]:  # 나의 지원서 순위가 더 낮으면
#                 temps.append(interviews[j])
#
#         for temp in temps:
#             if interviews[i] > temp:  # 나의 인터뷰 성적도 낮으면
#                 can_employed = False
#
#         if can_employed:
#             answer += 1
#
#     print(answer)