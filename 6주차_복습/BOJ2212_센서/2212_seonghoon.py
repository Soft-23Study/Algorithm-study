n = int(input())
k = int(input())
sensor = list(map(int, input().split()))

sensor.sort()
sub = [0] * (n-1)

for i in range(n-1):
    sub[i] = sensor[i+1] - sensor[i]

sub.sort()

answer = 0
for i in range(n-k):
    answer += sub[i]


print(answer)