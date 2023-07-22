# 근데 메모리를 너무 잡아먹는데 	229220 나 먹는디 이게 최선일까요?
# 평범한 배낭

import sys
input = sys.stdin.readline

#필요한 물건 수 n / 최대 k 만큼 무게
n,k = map(int,input().strip().split())


# 가치ㅣ 합의 최댓값

arr = [[]]

for i in range(n):
    arr.append(list(map(int, input().split())))

dp = [[0]*(k+1) for _ in range(n+1)]

for i in range(1, n+1):
    for j in range(1, k+1):
        w = arr[i][0]
        v = arr[i][1]
        if j < w:
            dp[i][j] = dp[i-1][j]
        else:
            dp[i][j] = max(dp[i-1][j], dp[i-1][j-w]+v)

print(dp[n][k])
