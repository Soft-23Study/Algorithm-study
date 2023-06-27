# 기초 자료구조

생성일: 2023년 6월 27일 오후 8:12

# 스택

- First In, Last Out 구조.
- 파이썬에서는 보통 리스트 or Deque을 이용하여 구현 가능.

![Untitled](../assets/1%EC%A3%BC%EC%B0%A8_%EC%9E%90%EB%A3%8C%EA%B5%AC%EC%A1%B0_%EC%8A%B9%ED%98%B8/Untitled.png)

### Stack in Python

> 전제 : box 라는 리스트 변수가 있다고 하자.
> 
- box.append(num) : box 리스트 마지막에 num 추가
- box.pop() : box 리스트 마지막에 있는 데이터 추출
    - 뽑혀진 데이터를 리턴 → 해당 값을 사용할 수 있다.
- box 스택의 Top 데이터 확인: box[-1]

```python
box = [1,2,3]

box.append(4) # 4 push
box.append(5) # 5 push

box.pop() # 5 pop
box.pop() # 4 pop
```

## 문제 접근법

1. 대놓고 스택 쓰라고 주는 문제
    - 대놓고 스택 쓰시면 됩니다.
    
    예) 스택(밑에꺼)
    
2. 뭔가가 연속적이다가 툭! 하고 끊길 때
3. 데이터를 계속 누적시키다가 특정 상황에서 갑자기 추출한다거나…

> 뭔가 누적되는 느낌을 주면서, 증가 / 감소 하는 부분에서 극댓값, 극솟값 부분을 기점으로 조건이 나뉠 때 스택을 많이 떠올리는 것 같다.
> 

### 관련 문제

1. 스택 (BOJ 10828)
    
    [10828번: 스택](https://www.acmicpc.net/problem/10828)
    
2. 올바른 괄호 (Programmers Lv.2)
    
    [올바른 괄호](https://school.programmers.co.kr/learn/courses/30/lessons/12909)
    
3. 탑
    
    [2493번: 탑](https://www.acmicpc.net/problem/2493)
    
4. [주식가격](https://school.programmers.co.kr/learn/courses/30/lessons/42584)
    - 문제 보기
        
        ![Untitled](../assets/1%EC%A3%BC%EC%B0%A8_%EC%9E%90%EB%A3%8C%EA%B5%AC%EC%A1%B0_%EC%8A%B9%ED%98%B8/Untitled%201.png)
        
    

    

# 큐

- First In, First Out
- Python에서는 보통 collections.deque를 이용하여 구현
    - deque : Double-Ended QUEue (양방향 큐)
        - 헤드에서도 푸시, 팝 되고, 테일에서도 푸시, 팝 된다.
    - collections.deque’s Time Complexity : O(1) ← Doubly Linked List

![Untitled](../assets/1%EC%A3%BC%EC%B0%A8_%EC%9E%90%EB%A3%8C%EA%B5%AC%EC%A1%B0_%EC%8A%B9%ED%98%B8/Untitled%202.png)

### Queue in Python

> 전제 : q라는 deque 빈 객체가 있다고 하자.
print(q) 해버리면 deque 객체로서 나오기 때문에, 결과 출력 시 list()로 형변환 해주면 Good!
> 
- q.append(num) : q의 마지막에 num 추가
- q.popleft() : q의 처음 데이터 하나 추출

---

- q.appendleft(num) : q의 처음에 num 추가
- q.pop() : q의 마지막 데이터 하나 추출
- q.clear() : q 데이터 싹 밀어버리기
- q.count(num) : q 데이터 안에 num이 몇개 있는지 카운팅

```python
from collections import deque

q = deque([])

q.append(1) # 1 push
q.append(2) # 2 push

q.popleft() # 1 pop
q.popleft() # 2 pop
```

## 문제 접근법

- 여러 데이터들에 대해서 순서를 따져야 할 때 한번쯤 떠올릴 법 하다.
- 특히, 주어진 데이터들을 “재사용” 해야 할 때 한번쯤 생각해보자.
    - 확인한 데이터를 다시 큐에 집어넣어서, 추후에 다시 확인해야할 때!
- 데이터를 연속적으로 받아들이다가 필터링 해야할 때
    - 1번 통과, 2번 통과, … 6번 통과, 7번 거절, 8번 통과 ….. 이런식으로
- 얘도 은근 대놓고 큐쓰라는 문제 많다.

### 관련 문제

1. 큐 (BOJ 10845)
    
    [10845번: 큐](https://www.acmicpc.net/problem/10845)
    
2. [프로세스](https://school.programmers.co.kr/learn/courses/30/lessons/42587)
    - 문제 보기
        
        ![Untitled](../assets/1%EC%A3%BC%EC%B0%A8_%EC%9E%90%EB%A3%8C%EA%B5%AC%EC%A1%B0_%EC%8A%B9%ED%98%B8/Untitled%203.png)
        
    
    
    

# 해시

- Key와 그에 상응하는 Value를 매핑해주는 자료구조.
- Python에서는 주로 Dictionary와 collections.Counter로 구현.

![Untitled](../assets/1%EC%A3%BC%EC%B0%A8_%EC%9E%90%EB%A3%8C%EA%B5%AC%EC%A1%B0_%EC%8A%B9%ED%98%B8/Untitled%204.png)

### Dictionary

[02-5 딕셔너리 자료형](https://wikidocs.net/16)

- 파이썬의 기본 자료구조 중 하나.
- {} (중괄호) 로 묶는다.

```python
studyTeam = {’승호’: 26, ‘지민’: 24, ‘성훈’: 25, '진행여부': True}

print(studyTeam['승호']) #26
print(studyTeam['지민']) #24

studyTeam['소현'] = 25

print(studyTeam['소현']) #25
```

### Counter

[파이썬 collections 모듈의 Counter 사용법](https://www.daleseo.com/python-collections-counter/)

- collections.Counter 함수
- 각 key들의 빈도 수를 카운팅 후 Value로 저장한다.

```python
from collections import Counter

Counter(["hi", "hey", "hi", "hi", "hello", "hey"])
>>> Counter({'hi': 3, 'hey': 2, 'hello': 1})

Counter("hello world")
>>> Counter({'h': 1, 'e': 1, 'l': 3, 'o': 2, ' ': 1, 'w': 1, 'r': 1, 'd': 1})
```

## 문제 접근법

1. 데이터들이 나온 빈도수를 가지고 조건을 따져야 할 때 유용.
2. 데이터를 스택, 큐로 저장하자니, 나중에 값을 찾을 때 순차적으로 1번부터 봐야할 것 같다..(시간복잡도 ㅠ)
    - 이럴 때, 자연스럽게 데이터들을 특정 값으로 “인덱싱” 하고 싶을 때 사용!

### 관련 문제

1. 완주하지 못한 선수
    
    [완주하지 못한 선수](https://www.notion.so/13a33869322048b7948158a9de05ebd1?pvs=21)
    
    [](https://school.programmers.co.kr/learn/courses/30/lessons/42576)
    

# 트리 (Tree)

[07. 파이썬으로 트리 구현하기](https://wikidocs.net/193702)

# 우선순위 큐 (Priority Queue)

[우선순위 큐(Prioirity Queue) (1) - 최대 힙 이용](https://velog.io/@holicme7/우선순위-큐Prioirity-Queue-mbk48cz764)

[파이썬의 우선순위 큐(PriorityQueue) 사용법](https://www.daleseo.com/python-priority-queue/)

- 일반적인 큐는 선형 구조를 가지지만(Linear Structure), 우선순위 큐는 트리 구조(Tree Structure)를 가진다.
- 나올 땐 우선순위가 높은 순서대로 나오는 방식.

# 힙

[[Python] 힙 자료구조 /  힙큐(heapq) / 파이썬에서 heapq 모듈 사용하기](https://littlefoxdiary.tistory.com/3)

> Heap(힙) : 무엇인가를 차곡차곡 쌓아올린 더미
> 

![Untitled](../assets/1%EC%A3%BC%EC%B0%A8_%EC%9E%90%EB%A3%8C%EA%B5%AC%EC%A1%B0_%EC%8A%B9%ED%98%B8/Untitled%205.png)

- 최소 힙 : 부모 노드보다 자식 노드가 항상 크다. → 루트엔 항상 최소값
- 최대 힙 : 부모 노드보다 자식 노드가 항상 작다. → 루트엔 항상 최대값

<aside>
⛔ heap 안에서 저장되어 있는 순서를 정렬되어 있다고 착각하면 안된다! (밑에서 계속)

</aside>

[heap의 생성과정 영상 보기](https://www.youtube.com/watch?v=VEYSSANa-cw)

## Heap in Python

> heapq 모듈을 사용하자. (최소 힙으로 구현되어 있다.)
> 
- heapq.heappush(heap, item) : item을 heap에 추가
- heapq.heappop(heap) : heap에서 가장 작은 원소 pop. 비어 있으면 IndexError
- heapq.heapify(x) : 리스트 x를 heap으로 변환한다. (x 리스트 내의 n개의 데이터를 일일이 변환하므로 O(N))

```python
import heapq

heap = []
heapq.heappush(heap, 50)
heapq.heappush(heap, 10)
heapq.heappush(heap, 20)

print(heap)
>>> [10, 50, 20]
```

### 최대 힙 구현하고 싶으면?

들어가는 원소에 -1을 곱해주면 된다. (Trick)

```python
heap_items = [1,3,5,7,9]

max_heap = []
for item in heap_items:
  heapq.heappush(max_heap, (-item, item))

print(max_heap)

>>> [(-9, 9), (-7, 7), (-3, 3), (-1, 1), (-5, 5)]
```

## 문제 접근법 (우선순위 큐 , 힙)

- 매 턴(Turn)마다 최소값을 가지고 (or 최대값을 가지고) 처리해야 하는 경우.
- 매 턴(Turn)마다 특정 조건에 의해 필터링 되거나 값을 뽑아내야 하는 경우.

### 관련 문제

1. [더 맵게](https://school.programmers.co.kr/learn/courses/30/lessons/42626)
    - 문제 보기
        
        ![Untitled](../assets/1%EC%A3%BC%EC%B0%A8_%EC%9E%90%EB%A3%8C%EA%B5%AC%EC%A1%B0_%EC%8A%B9%ED%98%B8/Untitled%206.png)
        
    
    