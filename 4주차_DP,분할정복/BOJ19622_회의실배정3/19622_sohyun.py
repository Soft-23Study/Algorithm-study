#회의실 배정3

import sys
input = sys.stdin.readline

n = int(input()) # 회의실

# 시작 / 끝 시간 & 회의 시간
# 회의 진행할 수 있는 최대 인원?

# 회의는 앞뒤와만 시간이 겹치므로 앞부터 찬찬히 선택하면서 값을 구해나가야한다는 부분이 dp

answer = 0
# 마지막으로 끝난 시간 _e
# 그 때의 인원 수 _p

# 초기 값 먼저 세팅
_s,_e,_p = map(int,input().strip().split())

dp = [0 for _ in range(n)]
dp[0]=_p 

# 시작
for i in range(1,n):
    s,e,p = map(int,input().strip().split())
    
    if i == 1 :
        dp[i] = max(dp[i-1],p)
    else:
        dp[i] = max(dp[i-2]+p , dp[i-1])

print(dp[n-1])
