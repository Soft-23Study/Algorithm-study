import sys; input = sys.stdin.readline
from  itertools import combinations

size, howMany = map(int, input().split())

Map = []

# 도시 지도 그리기
for _ in range(size):
    row = list(map(int, input().split()))
    Map.append(row)

chicken_info = []
house_info = []
distance_heap = []

for i in range(size):
    for j in range(size):
        if Map[i][j] == 1:
            house_info.append((i, j))
        elif Map[i][j] == 2:
            chicken_info.append((i, j))

# 풀지 못했기에 찾아봤음.... 처음에 heap을 사용해 구현하려고 하다가 점점 내용이 산으로 가서 결국 찾아봄..
# 조합에 대해서 반복문을 돌리는 방법도 배웠다..

result = 9999

for chi in combinations(chicken_info, howMany):  # howMany개의 치킨집 선택
    total = 0            # 도시의 치킨 거리
    for h in house_info:
        chi_len = 999   # 각 집마다 치킨 거리
        for j in range(howMany):
            chi_len = min(chi_len, abs(h[0] - chi[j][0]) + abs(h[1] - chi[j][1]))
        total += chi_len
    result = min(result, total)

print(result)