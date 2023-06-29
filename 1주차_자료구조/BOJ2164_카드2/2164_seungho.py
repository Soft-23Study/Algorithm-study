'''
# 스택으로 풀려고 했던 1st Try

n = int(input())
stack = list(range(n, 0, -1))

while len(stack)>1:
    stack.pop()
    top = stack[-1]
    stack.pop()
    stack.insert(0, top)
print(stack[0])
'''
'''
처음엔 스택을 생각해서 풀었는데, 가장 밑바닥에 하나를 추가하는 부분에서 막혔다.
두 가지 방법을 생각했는데,
1. 리스트 함수 (insert) 를 이용하여 꾸겨넣기
    -> 시간초과가 뜨네..?
2. collections.deque로 바꿔서 Doubly-Ended Queue로 풀기
    -> 시간초과 없이 정답 판정
'''
from collections import deque
n = int(input())
q = deque(list(range(n,0,-1)))
while len(q)>1:
    q.pop()
    top = q[-1]
    q.pop()
    q.appendleft(top)
print(q[0])