import sys

input = sys.stdin.readline

tc = int(input())
for _ in range(tc):
    num = int(input())
    logs = sorted(list(map(int, input().strip().split())))
    max_gap = max(abs(logs[0]-logs[1]), abs(logs[0]-logs[2]))
    if num%2==0:
        for i in range(1, num-2):
            max_gap = max(max_gap, abs(logs[i]-logs[i+2]))
        max_gap = max(max_gap, abs(logs[num-3]-logs[num-1]))
    else:
        for i in range(1, num-2):
            max_gap = max(max_gap, abs(logs[i]-logs[i+2]))
        max_gap = max(max_gap, abs(logs[num-1]-logs[num-2]))
    print(max_gap)

# 처음엔 입력된 배열들을 최적의 순서에 맞게 재배열해야한다는 관습적인 패턴으로 풀고자 했다. -> 30분정도 삽질하다 아님을 직시
# 이후, 재배열보다는 각 값들간의 차이의 최댓값만 구하면 된다는걸 깨닫고,
# 패턴에 맞게 최대값만 구한다음 계산한 결과 정답 처리