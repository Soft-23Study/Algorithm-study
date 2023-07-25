# Z

# 예제 예시보니 인덱스 값 r,c 인듯 0부터 시작 좌표식(r,c)

# 일단 이 지점이 2x2로 나눴을 때 어느 칸(2X2)인지 알아야함
# 칸 나눴을때 그 칸(2X2) 안에서 1234 중에서 어딘지 알아야함

# r=7 c=3 이면  (7,3)이 몇번째 칸에 있는지 ?
# 7/2했을 때 가아니라 문제 잘못이해햇네

# 일단 4칸으로 나누고 그안에서 또 4칸 나누니  재귀 쓰겠거니
# 4칸 중 어느 칸인지 판단을 하는 알고리즘 짜기
# AB 
# CD 라고 정해두고

import sys
input = sys.stdin.readline



def space(nn,r,c,count):


    if nn<2: # 하나 남음
        if r==0 and c == 0 :
            count+=0
        elif r==0 and c==1 :
            count+=1
        elif r==1 and c==0:
            count+=2
        elif r==1 and c==1:
            count+=3
        print(count)
        return count

    check_n = nn-1
    check_r = 2**check_n

    if r < check_r and c < check_r: #A
        space(check_n,r,c,count)
    elif r < check_r and c >= check_r: #B   
        space(check_n,r,c-2**check_n,check_r**2+count)
    elif r >= check_r and c < check_r: #C
        space(check_n,r-2**check_n,c,2*(check_r**2)+count)
    elif r >= check_r and c >= check_r:  #D 
        space(check_n,r-2**check_n,c-2**check_n,3*(check_r**2)+count)



n,r,c = map(int,input().split())
space(n,r,c,0)
