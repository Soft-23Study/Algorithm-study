n = int(input())

dp = [0] * 1_000_001

dp[1] = 1
dp[2] = 2

for i in range(3, n+1):
    dp[i] = (dp[i-2] + dp[i-1])% 15746

print(dp[n])


# 아래의 방법으로 할 경우 메모리초과 실패가 뜬다.
# int의 값이 크기 때문에 메모리초과가 난 것이라고 한다.

# n = int(input())
#
# dp = [0] * 1_000_001
#
# dp[1] = 1
# dp[2] = 2
#
# for i in range(3, n+1):
#     dp[i] = dp[i-2] + dp[i-1]
#
# answer = dp[n] % 15746
#
# print(answer)