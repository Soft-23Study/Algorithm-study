# 1. 입력받을때 input() 을 사용했더니 시간초과 -> sys.stdin.readline() 으로 바꿔줌!

# 2. 양수 힙, 음수 힙 두개 만들어서 관리해줌
#    => 음수 힙일 경우 최대힙 으로 구현줘야 함 -> 힙에 넣을때 부호 바꿔서 넣고, 뺄때 부호 다시 붙여주는 방식으로 최대힙 활용

# 3. 사람들 풀이 확인해보니 그냥 힙 하나에 (abs(num),num) 으로 관리하는 방법이 더 깔끔한거 같긴함 
#    => 튜플 비교 시 (a,b) 값이 있을 때 a 값을 먼저 비교하고, 그 후에 b 값을 비교하는 원리 활용

import heapq, sys

n = int(sys.stdin.readline())

pos_heap = []
neg_heap = []

for _ in range(n):
    x = int(sys.stdin.readline())

    if x == 0:
        if len(pos_heap) == 0 and len(neg_heap) == 0: print(0)
        else:
            if len(pos_heap) == 0: print(-heapq.heappop(neg_heap))
            elif len(neg_heap) == 0: print(heapq.heappop(pos_heap))
            else:
                if pos_heap[0] < neg_heap[0]: print(heapq.heappop(pos_heap))
                else: print(-heapq.heappop(neg_heap))
    elif x < 0: heapq.heappush(neg_heap,-x)
    else: heapq.heappush(pos_heap,x)
