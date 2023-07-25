a, b, c = map(int, input().split())

def cal(a, b, c):
    if b == 1:
        return a % c
    elif b % 2 == 0:
        return (cal(a, b//2, c) ** 2) % c
    else:
        return ((cal(a, b//2, c) ** 2) * a) % c

print(cal(a,b,c))