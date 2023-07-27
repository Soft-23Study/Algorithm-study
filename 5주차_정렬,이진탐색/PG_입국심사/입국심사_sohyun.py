# 범위와 기준을 잡는 것만 잘하면 구현은 어렵지 않은 
def solution(n, times):
    answer = 0
    start, end = 1,max(times)*n # 최대 시간 값


    while(start<=end):
        mid = (start+end)//2
        people=0
        for t in times:
            people+=mid//t # mid일때 수행할 수 있는 사람수 구하기
            if people >= n:
                break
            
        if people < n:
            start=mid+1
        elif people >= n :
            answer = mid
            end = mid -1

    return answer
