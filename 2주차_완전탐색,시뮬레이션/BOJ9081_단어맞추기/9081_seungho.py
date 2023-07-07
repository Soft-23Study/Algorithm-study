tc = int(input())

for i in range(tc):
    word = list(input())
    point = word[-1]
    answer = ""
    for i in range(len(word)-2, -1, -1):
        if ord(word[i]) < ord(point):
            # 앞 문자가 뒤 문자보다 작을때 (변곡점)
            min_word = word[i+1]
            min_word_idx = i+1

            #변곡점 단어 뒷단어부터 하나씩 보며 변곡점단어 보다는 큰 단어들 중 최소 단어를 찾는다.
            for w in range(i+2, len(word)):
                if ord(word[i]) < ord(word[w]) < ord(min_word):
                    min_word = word[w]
                    min_word_idx = w
            # 찾은 단어와 변곡점 단어를 update
            word[min_word_idx] = word[i]
            word[i] = min_word

            #정답 단어 갱신 : 원래단어 + 변곡점update 단어 + 뒷단어들 오름차순정렬
            answer = "".join(word[:i+1])
            for r in sorted(word[i+1:]):
                answer += r
            print(answer)
            break
        else:
            # 앞 문자가 뒤 문자보다 클때 (지나간다)
            point = word[i]
            # 마지막 단어라면 그대로 출력
            if i==0:
                print("".join(word))

'''
처음엔 순열/조합을 이용한 마구잡이 완전탐색인줄 알았는데 완전 다른 느낌의 유형이다.
완전탐색을 생각했다가 시간제한이 1초임을 보고 완탐 유형이 아님을 직감 -> 시간절약했다. (배운거 써먹은 느낌이라 좋았다)
그림으로 공식을 도식화한 후 바로 코드에 적용했지만 막상 구현단계에서 삽질을 좀 하느라 시간이 50분정도 걸림
'''


