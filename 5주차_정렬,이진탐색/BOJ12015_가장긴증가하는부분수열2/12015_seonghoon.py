# 너무 어려운데..?

n = int(input())
array = list(map(int, input().split()))
answer = [0]

for a in array:
    if answer[-1] < a:
        answer.append(a)
    else:
        low = 1
        high = len(answer) - 1
        while low < high:
            mid = (low + high) // 2
            if answer[mid] < a:
                low = mid + 1
            elif answer[mid] >= a:
                high = mid
            else:
                low = high = mid

        answer[high] = a

print(len(answer)-1)
