import sys

input = sys.stdin.readline

n = int(input())
k = int(input())
students_like = [0] * 101
pictures = []
pictures_idx = 1
recommend = list(map(int, input().strip().split()))
for rec in recommend:
    students_like[rec] += 1 #지목된 학생 추천수 +1
    pictures_idx += 1
    if len(pictures) < n:
        #사진틀 공간 남아있을 경우
        #[추천수, 오래된번호, 학생번호] 로 추가
        exist_flag = False
        for i in range(len(pictures)): #이미 사진틀에 있는 번호일 경우
            if pictures[i][2] == rec:
                pictures[i][0] = students_like[rec]
                exist_flag = True
                break
        if not exist_flag:
            pictures.append([students_like[rec], pictures_idx, rec])
    elif len(pictures) == n:
        #사진틀이 꽉찼을 경우
        exist_flag = False
        for i in range(len(pictures)):
            if pictures[i][2] == rec:
                # 현재 지목된 학생이 이미 사진틀에 있는 경우
                pictures[i][0] = students_like[rec]
                exist_flag = True
                break
        if not exist_flag:
            #사진틀에 없는 경우
            sorted_pictures = sorted(pictures)
            pictures.remove(sorted_pictures[0])
            pictures.append([students_like[rec], pictures_idx, rec])
            students_like[sorted_pictures[0][2]] = 0

result = []
for pic in pictures:
    result.append(pic[2])

for i in sorted(result):
    print(i, end=' ')









