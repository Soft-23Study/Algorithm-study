import sys
input = sys.stdin.readline
 
n = int(input())
sol = list(map(int, input().split()))
sol.sort()
 
start = 0
end = n - 1
 
result = abs(sol[start] + sol[end])
answer = [sol[start], sol[end]]
 
while start < end:
    sum = sol[start] + sol[end]
 
    if abs(sum) < result:

        result = abs(sum)
        answer = [sol[start], sol[end]]

        if result == 0:
            break

    if sum < 0:
        start += 1
    else:
        end -= 1
 
print(answer[0], answer[1])
