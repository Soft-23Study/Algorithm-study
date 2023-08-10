# 30

# 10의 배수이면서 3의 배수여야함
# 10의 배수는 끝자리 0 -> 0이 하나이상 존재
# 각 자리 합이 3의 배수 -> %3 값 == 0 

import sys
input = sys.stdin.readline
n = input().strip() # 애초에 문자열로 받음

if n.find('0') == -1 :
    print(-1)
else:
    sum = 0
    for i in n:
        sum += int(i)
    if sum%3 !=0 :
        print(-1)
    else:        
        print(''.join(sorted(n,reverse=True)))
