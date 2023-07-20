# ---------------------------------------------------- 1트 => 틀림
n = int(input())
t = [0]
p = [0]
for _ in range(n):
    _t,_p = map(int,input().split())
    t.append(_t)
    p.append(_p)

dp = [0] * (n+1)

if t[1] <= n:
    dp[1] = p[1]

for i in range(2,n+1):
    #print("============= i: ",i)
    if i+t[i]- 1 <= n:                          # 기간 내 수행 가능이라면
        for j in range(i-1,-1,-1):
            if j+t[j]-1 < i:                
                dp[i] = max(dp[i],dp[j]+p[i])   # 현재 상담 수행
        dp[i] = max(dp[i], dp[i-1])             # 현재 상담 수행하기 || 수행 안하기 중 이득인거 선택
    else:
        dp[i] = dp[i-1]
    #print("--- dp:",dp)

print(dp[n])

# ---------------------------------------------------- 2트 => 성공
n = int(input())
t = [0]
p = [0]
for _ in range(n):
    _t,_p = map(int,input().split())
    t.append(_t)
    p.append(_p)

dp = [0] * (n+1)

for i in range(1,n+1):
    if i+t[i]-1 <= n:                                            # 기간 내 수행 가능이라면
        dp[i+t[i]-1] = max(dp[i+t[i]-1], dp[i-1]+p[i])           
    dp[i] = max(dp[i], dp[i-1])         

print(dp[n])