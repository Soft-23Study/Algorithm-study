from collections import deque

t = int(input())

for _ in range(t):
    n = int(input())
    arr = list(map(int,input().split()))

    arr.sort()
    ans_arr = deque([arr.pop()])

    flag = 0
    while arr:
        if flag == 0:
            ans_arr.append(arr.pop())
            flag = 1
        else:
            ans_arr.appendleft(arr.pop())
            flag = 0
    
    answer = 0
    for i in range(n-1):
        answer = max(answer, abs(ans_arr[i]-ans_arr[i+1]))
    answer = max(answer, abs(ans_arr[0]-ans_arr[n-1]))
    
    print(answer)