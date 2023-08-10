# 백준 채점 10%에서 틀렸다고 메세지가 뜬다.
# 근데 내가 수동으로 입력한 30가지의 testcase는 정답코드와 답이 같다..
# 어디서 잘못된건지 도저히 모르겠음

import math
k = int(input())

# 몇번째의 반대인지 알아내는 함수
def process(index):
    # 1번째나 2번째일 경우, 그 위치에 해당하는 값을 return
    if index == 1:
        return 0
    elif index == 2:
        return 1

    n = math.floor(math.log2(index))  # 2의 n제곱 < k < 2의 n+1제곱

    # 20번째라면, 20 - 16 = 4를 하여, index가 4인 자리를 살펴볼 것인데, 이 경우 16이 minus_value에 해당
    minus_value = math.pow(2, n)

    # 2의 지수 형태일 경우, 절반만 뺌 (예를 들어 16일 경우, 16 - 8 을 하여 index가 8인 자리를 살피기 위함)
    if minus_value == index:
        t = index - minus_value // 2
    # 그 외의 경우
    else:
        t = index - minus_value

    # 그 위치에 해당하는 값
    m = process(t)

    # 값을 뒤집어야만, 내가 구하고자 하는 위치의 값을 알 수 있다.
    if m == 1:
        return 0
    elif m == 0:
        return 1

print(process(k))


