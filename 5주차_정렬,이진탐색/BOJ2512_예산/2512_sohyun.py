import sys

input=sys.stdin.readline()

n = int(input())
money = list(map(int, input()))
m = int(input())

_max = max(money) 
_min = 1 

while _max >= _min:
    mid = (_max + _min) // 2 
    sum = 0 

    for i in money:
        if mid < i:
            sum += mid
        else:
            sum += i
    if sum > m:
        _max = mid - 1
    else:
        _min = mid + 1

print(_max)
