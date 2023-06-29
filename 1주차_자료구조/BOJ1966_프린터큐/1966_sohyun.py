#프린터 큐

# 문제읽는 순간 중요도 단어 언급되므로 당연히 우선순위 큐 ! 
# 중요도 높은 문서 있다면 queue의 가장뒤에 배치
# 아니라면 바로 인쇄

# 1st algorithm
from collections import deque

k = int(input()) #테스트케이스의 수
for j in range(k):
    p_answer=0
    n,m= map(int,input().split()) # n:문서의 갯수 / m번째 인덱스가 몇번째 출력인지 궁금함
    im_list = deque(map(int,input().split())) # 중요도 리스트
    in_list = deque(range(0,n)) #인덱스 리스트
    p_a = 0
    for i in range(n):
        point=(-1)*int(im_list.index(max(im_list)))
        im_list.rotate(point)
        in_list.rotate(point)
        if in_list[0]==m:
            p_answer=p_a+1
            print(p_answer)
            break
        in_list.popleft()
        im_list.popleft()
        p_a+=1


# 총평 : 보자마자 든 생각은 rotate를 쓰면 좋겠다는 것이어서 deque를 사용하였고
#       인덱스를 처리하는 방법에서 고민을 많이했는데 애초에 중요도 rotate와
#       같이 돌려주면 너무 쉽게 구하는게 가능해서 이 방식으로 구함
