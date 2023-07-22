n, max_w = map(int, input().split())

items = [0] * (n+1)
weights = [0] * (n+1)
dp = []
dp.append([0] * (max_w + 1))

for i in range(1, n+1):
    weights[i], items[i] = map(int, input().split())

    row_of_dp = [0] * (max_w + 1)
    dp.append(row_of_dp)

for i in range(1, n+1):
    for w in range(1, max_w+1):
        if weights[i] > w:
            dp[i][w] = dp[i-1][w]
        else:
            dp[i][w] = max(dp[i-1][w], dp[i-1][w-weights[i]] + items[i])

print(dp[n][max_w])