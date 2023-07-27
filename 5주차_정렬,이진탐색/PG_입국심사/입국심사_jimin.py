# ----------------------------------------------------
# 1. 예전에는 디게 어렵다고 생각했는데, 지금 보니 '랜선자르기' 문제랑 똑같은 원리
# 2. start,end,mid 값을 '시간' 으로 잡는다는게 point
# 3. '랜선 자르기' 도, 이 문제도 조건을 만족하는 mid 값을 발견해도 answer 값에 담아두기만 하고 탐색은 계속 해 나가야 한다는 것이 중요
#    => 발견한 mid 값이 최대/최소 조건도 만족하는지는 모르기 때문
# ----------------------------------------------------
def solution(n, times):
    answer = 0
    
    start = 1
    end = min(times) * n
    
    while start <= end:
        mid = (start + end) // 2
        
        done_cnt = 0
        for time in times:
            done_cnt += mid // time
        
        if done_cnt >= n:
            answer = mid
            end = mid - 1
        else:
            start = mid + 1
    
    return answer