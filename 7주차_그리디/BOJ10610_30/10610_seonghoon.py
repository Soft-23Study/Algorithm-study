# 가장 큰 수부터 일일이 하나씩 순열을 이용해 조건문을 사용해볼까 했지만 '수학'문제였던 것

n = list(map(int, input()))

if 0 in n:
    if sum(n) % 3 == 0:
        n.sort(reverse=True)
        print(''.join(map(str, n)))
        exit(0)

print(-1)

