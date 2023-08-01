n = int(input())
fluids = list(map(int, input().split()))

fluids.sort(reverse=True)

start = 0
end = n - 1
min = 2_000_000_000
answer = [0] * 2

while start < end:
   sum = fluids[start] + fluids[end]

   if abs(sum) < min:
       min = abs(sum)
       answer[0] = fluids[start]
       answer[1] = fluids[end]

   if sum == 0:
       break

   if sum > 0:
       start += 1
   if sum < 0:
       end -= 1

print(answer[1], answer[0])