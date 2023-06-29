from collections import deque

tc = int(input())
for _ in range(tc):
    n, m = map(int, input().split()) #n: 문서의 개수, m: 몇번째 인쇄
    prior = deque(list(map(int, input().split())))
    count = 0

    while True:
        cur_prior = prior.popleft()
        m-=1
        if len(prior)==0:
            print(count+1)
            break
        if cur_prior < max(prior):
            prior.append(cur_prior)
            if m<0:
                m = len(prior)-1
        else:
            count += 1
            if m<0:
                print(count)
                break
'''
1st Try: 큐 속의 데이터들을 [(인덱스1, 중요도1), (인덱스2 중요도2), ...]
이런 형태로 잡았는데, 결국 타겟 위치를 인덱싱 하는데 해매다가 문제풀이를 본 케이스...
현재 데이터의 큐에서의 위치를 변수로 계속 추적해주며 찾는 방법을 알았다.
'''
