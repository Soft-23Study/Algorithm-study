# ----------------------------------------------------
# 1. 예전엔 dfs + 백트래킹으로 하느라 고생했는데 조합으로 하니 굳
#    => 근데 시간복잡도적으로 괜찮은 이유는 모르겠음.. 
#       ex. n = 50, m = 13 인 경우에 워스트 케이스로 2500C3 되면 안되야 되는거 아닌가 ??
# ----------------------------------------------------
from itertools import combinations

n,m = map(int,input().split())
_map = []
for _ in range(n):
    _map.append(list(map(int,input().split())))

house = []
chicken = []

for i in range(n):
    for j in range(n):
        if _map[i][j] == 1: house.append((i,j))
        elif _map[i][j] == 2: chicken.append((i,j))

chick_comb = combinations(chicken,m)

answer = 1e9
for selected_chickens in chick_comb:
    total_dist = 0
    for (h_i,h_j) in house:
        dist = 1e9
        for (c_i,c_j) in selected_chickens: 
            dist = min(dist,abs(h_i-c_i) + abs(h_j-c_j))
        total_dist += dist
    answer = min(answer,total_dist)

print(answer)