n = int(input())
liqs = list(map(int,input().split()))

liqs.sort()

start = 0
end = n-1

_min = abs(liqs[start]+liqs[end])
ans_start, ans_end = liqs[start], liqs[end]

while start < end:
    _sum = liqs[start] + liqs[end]

    if abs(_sum) < _min:
        _min = abs(_sum)
        ans_start, ans_end = liqs[start], liqs[end]
    
    if _sum < 0: start += 1
    else: end -= 1

print(ans_start,ans_end)
