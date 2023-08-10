n = input()

splited_nums = list(map(int,n))

if 0 not in splited_nums:
    print(-1)
    exit()

if sum(splited_nums) % 3 != 0:
    print(-1)
    exit()

splited_nums.sort(reverse=True)

answer = ""
for num in splited_nums:
    answer += str(num)

print(int(answer))