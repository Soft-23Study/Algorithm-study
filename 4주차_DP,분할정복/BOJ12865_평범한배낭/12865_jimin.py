# ---------------------------------------------------- 1트 => 틀림. 왜 틀렸지 ??
# n,k = map(int,input().split())
# w = []
# v = []
# for _ in range(n):
#     _w,_v = map(int,input().split())
#     w.append(_w)
#     v.append(_v)

# dp_things = [[0] * 2 for _ in range(n)]      # (w,v) i 번째 물품까지 담았을 때의 가방 상태
# dp_weights = [0] * (100001)                  # 각각 무게에서의 최대값

# for i in range(n):
#     _w,_v = w[i], v[i]
#     dp_weights[_w] = _v

# if w[0] <= k:
#     dp_things[0][0] = w[0]
#     dp_things[0][1] = v[0]

# for i in range(1,n):
#     # i 번째 물품을 문제없이 추가로 담을 수 있는 경우
#     if dp_things[i-1][0] + w[i] <= k:
#         dp_things[i][0] = dp_things[i-1][0] + w[i]
#         dp_things[i][1] = dp_things[i-1][1] + v[i]
#         dp_weights[dp_things[i][0]] = max(dp_weights[dp_things[i][0]], dp_things[i][1])
#     else:
#         # i 번째 물품을 담지 않는 경우
#         _w, _v = dp_things[i-1][0], dp_things[i-1][1]
#         # i 번째 물품을 담는 경우
#         i_w, i_v = 0,0
#         for j in range(k+1-w[i]):
#             i_w = max(i_w, j + w[i])
#             i_v = max(i_v, dp_weights[j] + v[i])
        
#         if _v > i_v:
#             dp_things[i][0] = _w
#             dp_things[i][1] = _v
#         elif _v == i_v:
#             if _w <= i_w:
#                 dp_things[i][0] = _w
#                 dp_things[i][1] = _v
#             else:
#                 dp_things[i][0] = i_w
#                 dp_things[i][1] = i_v
#         else:
#             dp_things[i][0] = i_w
#             dp_things[i][1] = i_v
#         dp_weights[dp_things[i][0]] = max(dp_weights[dp_things[i][0]], dp_things[i][1])
    
# print(dp_things[n-1][1])


# ---------------------------------------------------- 2트 => 답 참고
# 1. 0-1 knapsack problem: 선택지가 물건을 담을수 있고/없고 이분법적으로 나누어짐.
# 2. dp[n][k]: n 번째 물건 까지 살펴보았을 때, 무게가 k 인 배낭의 최대 가치
# 3. 로직
#    : "현재 배낭의 허용 용량 < 넣을 물건의 무게" 이면, 넣을 수 없다.
#       a) 현재 넣을 물건의 무게만큼을 배낭에서 빼고, 현재 물건 넣기
#       b) 현재 물건을 넣지 않기
#    => a,b 중 더 좋은걸 선택
# ---------------------------------------------------- 
n,k = map(int,input().split())

things = [[0,0]]
dp = [[0]*(k+1) for _ in range(n+1)]

for i in range(n):
    things.append(list(map(int,input().split())))

for i in range(1,n+1):
    for j in range(1,k+1):
        w = things[i][0]
        v = things[i][1]

        if j < w:
            dp[i][j] = dp[i-1][j]
        else:
            dp[i][j] = max(dp[i-1][j],dp[i-1][j-w]+v)

print(dp[n][k])