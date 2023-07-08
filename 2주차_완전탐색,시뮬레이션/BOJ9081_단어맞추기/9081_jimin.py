# ----------------------------------------------------
# 1. '순열 없이 사전순 다음 수 구하기' 로직 핵심
#     => 대충 어디서 봤던 거 같긴 한데 명확한 로직이 생각안나서 로직 참고함
#     => 앞으로는 까먹지 말자 !!!
# 2. join 함수 문법 까먹지 말자
# 3. 파이썬에서 배열 부분적으로 정렬할때 arr[:i].sort() 안먹힘. sorted 로 따로 빼서 배열 만들고 연결해줘야 한다!
# ----------------------------------------------------
t = int(input())

def get_next():
    global word
    for i in range(len(word)-2,-1,-1):
        if word[i] < word[i+1]:
            for j in range(len(word)-1,i,-1):
                if word[i] < word[j]:
                    word[i], word[j] = word[j], word[i]
                    #word[i+1:].sort()   => 안먹힘!!!
                    sorted_part = sorted(word[i+1:])
                    word = word[:i+1] + sorted_part
                    return

for _ in range(t):
    word = list(input())
    get_next()
    print("".join(word))