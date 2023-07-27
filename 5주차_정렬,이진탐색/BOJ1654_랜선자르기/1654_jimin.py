# ----------------------------------------------------
# 1. 랜선의 길이가 최대 2^31-1 이므로 브루트포스로는 탐색할 수 없는 범위이다.
# 2. O(logN) 의 시간복잡도를 위해 이분탐색을 쓴다!
# ----------------------------------------------------
k,n = map(int,input().split())
lens = []
for _ in range(k):
    lens.append(int(input()))

lens.sort()

start = 1
end = lens[-1]
answer = 0

while start <= end:
    mid = (start + end) // 2

    cnt = 0
    for l in lens: cnt += l // mid

    if cnt >= n:
        answer = max(answer,mid)
        start = mid + 1
    else:
        end = mid - 1

print(answer)