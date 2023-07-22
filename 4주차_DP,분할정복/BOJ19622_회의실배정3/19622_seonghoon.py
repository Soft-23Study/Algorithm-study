# " 임의의 회의 K(1≤ K ≤ N)는 회의 K − 1과 회의 K + 1과는 회의 시간이 겹치고 다른 회의들과는 회의 시간이 겹치지 않는다. " 라는 조건때문에 매우 쉽게 풀었던 문제
# 만약 위 조건이 없었다면 엄청 어려웠을 것 같다.
# i번째 회의를 할 경우, i-2번째에서의 최댓값에 회의 인원을 더해주고
# i번째에 회의를 안 할 경우, i-1번째에서의 최댓값을 이어받는다.

n = int(input())

people = [0] * (n+1)
for i in range(1, n+1):
    start_time, end_time, num_people = map(int, input().split())
    people[i] = num_people

dp = [0] * (n+1)
dp[1] = people[1]

for i in range(2, n+1):
    dp[i] = max(dp[i-2] + people[i], dp[i-1])

print(dp[-1])