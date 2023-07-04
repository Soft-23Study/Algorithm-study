# 괄호의 값

# () , [] 올바른 괄호열
# x : 올바른 괄호열이면 (x) ,[x]도 올바른 괄호열
# x,y모두 올바른 괄호열이면 xy도 올바른 괄호열

# () = 2
# [] = 3
# (x) = 2 * 값x
# [x] = 3 * 값x
# xy 괄호값 = x+y
# 괄호값 구해라

import sys

cal = sys.stdin.readline().rstrip()

arr = []

val = 1
answer = 0
tf = True # 예외 경우 걸러주는 용도

for i, str in enumerate(cal):
    if str == "(":
        arr.append(str)
        val *= 2

    elif str == "[":
        arr.append(str)
        val *= 3

    elif str == ")":
        if not arr or arr[len(arr) - 1] == "[":
            tf = False
            break
        if cal[i-1] == "(":
            answer += val
        arr.pop()
        val //= 2

    elif str == "]":
        if not arr or arr[len(arr) - 1] == "(":
            tf = False
            break
        if cal[i-1] == "[":
            answer += val
        arr.pop()
        val //= 3

if not tf or arr:
    print(0)
else:
    print(answer)

# 경우의수를 분리하는 것이 어려웠음 -> 까다로움
# 정리해서 분류
# 노가다로 한 느낌인데 더 찾아보면 좋은 알고리즘이 있지 않을까 추가로 알아볼 예정
