n = int(input())
k = int(input())
sensors = list(map(int,input().split()))

sensors.sort()

dist = []
for i in range(len(sensors)-1):
    dist.append(sensors[i+1]-sensors[i])

dist.sort()

for _ in range(k-1):
    dist.pop()

print(sum(dist))