# 곱셈

# 문제는 간단한데  당연히 A를 B번 곱하고 나누면 안될걸 알면서 도전후 역시나 시간 초과

# 분할 정복 이용해보기 
# 나눠서 계산하고 합치기 --> 코드 
import sys
input = sys.stdin.readline

a,b,c = map(int,input().split()) # a^b%c

def mul(a,b,c):

    # 예외처리
    if b == 1:
        return a % c

    # 반반 나눠서 하는데 홀수로 나눠진건 한번더 곱해줘야함
    if b % 2 == 0:
        return (mul(a,b//2,c)**2)%c
    else:
        return ((mul(a,b//2,c)**2)*a)%c



print(mul(a,b,c))
