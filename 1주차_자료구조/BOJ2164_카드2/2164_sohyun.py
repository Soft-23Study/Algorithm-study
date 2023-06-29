# 카드2

# N장의 카드 1~N (1이 위 , N번 카드가 아래 순서대로 카드 놓임)
# 맨 위 카드를 바닥에 버리고
# 그 다음 제일 위 카드를 제일 아래로 보냄
# 카드 1장 남을 때까지 반복

#answer
#3. deque 라이브러리 이용
from collections import deque

n = int(input()) # n : 카드의 갯수 (1~n)
que_card = deque(range(1, n+1))
while n > 1:
    que_card.popleft() # 맨 첫번째꺼 지우고
    que_card.rotate(-1) # rotate함수로 왼쪽 회전 시킴 -> 간단
print(que_card[0])

# 2번 방법보다 시간 17초 단축됨 -> 가장 효율적

#총평 : 시작/끝 값 넣고 빼는데 가장 효율적인 연산속도 -> deque
#       연산량 많을땐 list보다 deque

# 첫 문제다 보니 list , queue , answer 모두 써보기로 결정
# 1st 알고리즘 구상
# 버리기 + 선입선출(queue) 로 반복문 돌리면 돌아가겠네

# # 1. list로 구현
# n = int(input()) # n : 카드의 갯수 (1~n)

# queue_card = []

# # queue에 담아서 리스트 초기화
# for i in range(1,n+1) :
#     queue_card.append(i) 

# while n>1:
#     queue_card.pop(0)
#     queue_card.append(queue_card[0])
#     queue_card.pop(0)
#     n-=1


# print(*queue_card) #대괄호없이 리스트 출력 
# # 시간 초과 오류 발생 -> 리스트로 구현하면 시간 복잡도가 높아져 비효율적

#2. queue 라이브러리 사용
# from queue import Queue

# n = int(input()) # n : 카드의 갯수 (1~n)
# que_card=Queue()

# for i in range(1,n+1):
#     que_card.put(i)

# while n>1 : 
#     que_card.get()
#     move_card = que_card.get()
#     que_card.put(move_card)
#     n-=1
    
# print(que_card.queue[0]) 
# 백준으로 풀었을때 성공은 나오나 시간이 19초나 소요됨
