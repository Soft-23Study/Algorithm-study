import sys
input = sys.stdin.readline

tests = int(input())

for _ in range(tests):
    num = int(input())
    score = [list(map(int, input().split())) for _ in range(num)]

    score.sort(key=lambda x: x[0]) # 정렬 방식 람다 써먹기 ***

    min = score[0][1]
    answer = 1
    for i in range(1,num): 

        if score[i][1] < min:
            min = score[i][1]
            answer += 1
    print(answer)
