# 투에-모스 문자열
# 투에-모스 수열 구글링 참고했는데 수열 점화식 애초에 모르면 어떻게 풀까

import sys
input = sys.stdin.readline

k = int(input())

# t(0) = 0
# t(2n) = t(n)
# t(2n + 1) = 1 - t(n)

def find(x):
    if x == 0:
        return 0

    elif x == 1:
        return 1

    elif x % 2 == 0:
        return find(x // 2)

    else:
        return 1 - find(x // 2)


print(find(k - 1))
