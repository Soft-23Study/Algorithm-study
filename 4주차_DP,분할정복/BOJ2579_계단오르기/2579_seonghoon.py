import sys

input = sys.stdin.readline

n = int(input().strip())

stairs = []

for _ in range(n):
    stairs.append(int(input()))

dp = [0] * n

dp[0] = stairs[0]
if n > 1: dp[1] = stairs[0] + stairs[1]

for i in range(2, n):
    dp[i] = max(dp[i-2], dp[i-3] + stairs[i-1]) + stairs[i]

print(dp[-1])