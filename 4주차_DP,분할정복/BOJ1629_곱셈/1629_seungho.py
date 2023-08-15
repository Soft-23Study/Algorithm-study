a, b, c = map(int, input().split())
dp = [0] * (b+1)

dp[1] = a%c
for i in range(2, b+1):
    dp[i] = (dp[i-1]*a) % c

print(dp[b])