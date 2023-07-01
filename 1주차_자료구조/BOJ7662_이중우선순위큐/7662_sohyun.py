# 이중 우선순위 큐

# 데이터 삭제 : 연산 명령에 따라 우선순위 높/낮 데이터 삭제
# 이중 우선순위 큐 Q (Only 정수로 표현된 우선 순위)
# 연산 적용한 Q가 최종Q => 이때 최댓값 최솟값 출력


# 1st algorithm
# 최대힙과 최소힙을 수시로 둘다 반영되도록 바꿔주면서
# 구해나간다

import sys,heapq

T = int(sys.stdin.readline()) # 테스트 케이스 수

for i in range(T):

    k = int(sys.stdin.readline()) # 연산의 개수
    min_heap, max_heap = [], []
    visited = [False] * k

    for j in range(k):
        C, num = sys.stdin.readline().split()

        if C == 'I': # input인 상황
            heapq.heappush(min_heap, (int(num), j))
            heapq.heappush(max_heap, (-int(num), j))
            visited[j] = True

        else:
            if num == '1':
                while max_heap and not visited[max_heap[0][1]]:
                    heapq.heappop(max_heap)
                if max_heap:
                    visited[max_heap[0][1]] = False
                    heapq.heappop(max_heap)
            else:
                while min_heap and not visited[min_heap[0][1]]:
                    heapq.heappop(min_heap)
                if min_heap:
                    visited[min_heap[0][1]] = False
                    heapq.heappop(min_heap)

    while min_heap and not visited[min_heap[0][1]]:
        heapq.heappop(min_heap)
    while max_heap and not visited[max_heap[0][1]]:
        heapq.heappop(max_heap)

    if not min_heap or not max_heap:
        print("EMPTY")
    else:
        print (-max_heap[0][0],min_heap[0][0])

                










