# ---------------------------------------------------- 1트 => 시간초과
# 1. 최대값 pop -> max heap 으로 변환한 뒤 pop 해주는 방식
# 2. O(n^2) 이므로 당연히 시간초과,,
#    => 각각의 테케에 대해 O(n) 미만으로 바꿔야 함
#    => 최대힙, 최소힙 두개 쓰고싶음. 근데 둘 간 동기화 어떻게? 모르겠음.
# ----------------------------------------------------
# import sys, heapq

# t = int(sys.stdin.readline())

# def max_heap_pop():
#     max_heap = []
#     for _ in range(len(heap)): heapq.heappush(max_heap,-heapq.heappop(heap))

#     max_num = -heapq.heappop(max_heap)

#     for _ in range(len(max_heap)): heapq.heappush(heap,-heapq.heappop(max_heap))

#     return max_num

# for _ in range(t):
#     k = int(sys.stdin.readline())
#     heap = []

#     for _ in range(k):
#         command, num = sys.stdin.readline().split()

#         if command == "I": heapq.heappush(heap,int(num))
#         else:
#             if heap:
#                 if int(num) == -1: heapq.heappop(heap)
#                 else: max_heap_pop()
    
#     if heap:
#         min_ans = heapq.heappop(heap)
#         max_ans = max_heap_pop()
#         print(max_ans, min_ans)
#     else:
#         print("EMPTY")

# ---------------------------------------------------- 2트 => 답 참고
# 1. 튜플의 2번째 원소로 id 값을 넣어서 이 값을 토대로 최대힙, 최소힙 간 동기화
#    => id 값: 몇 번째 원소인지
# 2. visited 배열을 만들어서 i 번째 원소가 삭제되었는지, 아닌지 확인하며 동기화 가능  << 요게 이 문제의 포인트!
# 3. pop 할 때는 상대방 힙에 의해 삭제된 원소들을 미리 pop 해 준뒤, 내가 pop 하고 싶은 거 pop + visited True 변경 처리
# ----------------------------------------------------
import sys, heapq

t = int(sys.stdin.readline())

for _ in range(t):
    k = int(sys.stdin.readline())

    min_heap = []
    max_heap = []
    visited = [False] * k

    for i in range(k):
        command, num = sys.stdin.readline().split()

        if command == "I": 
            heapq.heappush(min_heap,(int(num),i))
            heapq.heappush(max_heap,(-1*int(num),i))
        else:
            if int(num) == -1:
                while min_heap and visited[min_heap[0][1]]: heapq.heappop(min_heap)
                if min_heap: 
                    visited[min_heap[0][1]] = True
                    heapq.heappop(min_heap)
            else:
                while max_heap and visited[max_heap[0][1]]: heapq.heappop(max_heap)
                if max_heap:
                    visited[max_heap[0][1]] = True
                    heapq.heappop(max_heap)
    
    while min_heap and visited[min_heap[0][1]]: heapq.heappop(min_heap)
    while max_heap and visited[max_heap[0][1]]: heapq.heappop(max_heap)
            
    if min_heap and max_heap:
        print(-heapq.heappop(max_heap)[0], heapq.heappop(min_heap)[0])
    else:
        print("EMPTY")