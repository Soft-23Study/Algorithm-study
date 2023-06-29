## 76 ms ##

from collections import deque

test_count = int(input())

for i in range(0,test_count):
    n, m = map(int, input().split())  # 문제에서의 N, M을 입력받음
    queue = deque()
    element_list = map(int, input().split())  # 중요도 값들을 입력받음
    index = -1

    # 중요도와 index를 tuple 형태로 deque에 추가함
    for element in element_list:
        index = index + 1
        queue.append((element, index))

    answer = 0

    # 실행 logic
    while True:
        (popped_element, popped_index) = queue.popleft()
        has_priority = True

        # 꺼낸 값보다 우선순위가 높은 값이 존재한다면 has_priority = False
        for (other_element, other_index) in queue:
            if popped_element < other_element:
                has_priority = False
                break

        # 꺼낸 값이 우선권을 가질 경우, 갖지 않을 경우 처리
        if not has_priority:
            queue.append((popped_element, popped_index))
        else:
            answer = answer + 1
            # 만약 우선권을 가졌는데, index값이 우리가 찾고자 하는 값이었다면 종료
            if popped_index == m:
                break

    print(answer)





