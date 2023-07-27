def solution(n, times):
    answer = 0
    left = 0
    right = max(times) * n  # 가장 클 때는 가장 오래걸리는 심사관에게 모두 입국심사를 받는 경우이기 때문에.

    while left <= right:
        mid = (left + right) // 2

        people = 0
        for time in times:
            people += mid // time

        if people >= n:
            right = mid - 1
            answer = mid
        else:
            left = mid + 1

    return answer

