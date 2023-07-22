import sys

n = int(sys.stdin.readline())

start = []
end = []
people = []
for _ in range(n):
    s,e,p = map(int,sys.stdin.readline().split())
    start.append(s)
    end.append(e)
    people.append(p)

dp = [0] * n

dp[0] = people[0]

if n > 1:
    if end[0] <= start[1]: 
        dp[1] = dp[0] + people[1]
    else:
        dp[1] = max(dp[0],people[1])

for i in range(2,n):
    # 이전 회의와 겹치지 않는 경우
    if end[i-1] <= start[i]:
        dp[i] = dp[i-1] + people[i]
    # 이전 회의와 겹치는 경우
    else:
        dp[i] = max(dp[i-1],dp[i-2]+people[i])

print(dp[-1])