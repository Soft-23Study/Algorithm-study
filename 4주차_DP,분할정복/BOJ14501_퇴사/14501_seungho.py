n = int(input())
terms = [-1]*(n+1)
profits = [-1]*(n+1)

dp = [0]*(n+2) #day 작업량 제외, 전까지의 최대 이익을 저장
buffer = [[] for _ in range(n+2)]

for i in range(1,n+1):
    terms[i], profits[i] = map(int, input().split())
    if i + terms[i] <= n+1:
        buffer[i+terms[i]].append(i)
print(buffer)

dp[1] = 0

for day in range(2, n+1):
    if buffer[day]:
        #buffer에 값이 들어있을 때
        for buf in buffer[day]:
            dp[day] = max(dp[buf]+profits[buf], max(dp[1:day+1]))
    else:
        #buffer에 값이 없을 때
        dp[day] = max(dp[1:day+1])
result = 0
print(dp) # 각각의 날에 작업한 프로핏을 더하지 않은 값. 왜냐하면 해당 날에 작업한 기간이 1일인지 며칠이 걸리지 모르기 때문에.

for day in range(1, n+1): #1일째부터 n일째까지를 계속 돌아보면서
    if day+terms[day]<=n+1: #day(해당일) + terms[day](해당일자의 작업의 기간) <= n+1보다 작으면, 다시말해서 해당 일자에 작업을 시행할 수 있으면,
        result = max(result, dp[day]+profits[day]) # 결과값을 여태까지의 최대 이익과 vs (현재 날의 최댓값 + 현재 날에서 작업을 했을 때 얻는 이득)을 비교해서 최댓값을 얻는다.
        print(dp, profits, result)

print(result)
