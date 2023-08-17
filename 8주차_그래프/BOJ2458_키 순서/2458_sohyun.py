# 키 순서

# 가중치 없어서 BFS도 가능하지 않을까 생각 => 모르겠음
# 플로이드워셜 => 앞서 푼 문제도 그렇고 이거 쓴 알고리즘은 다 시간초과나서 풀이보니까 pypy다들 돌렸던데 괜찮은건지..? 시간 초과 고려하면 대부분 다익스트라로,,?

import sys
input = sys.stdin.readline


n, m = map(int, input().split()) # 학생 수  / 비교 횟수
graph = [[0]*(n+1) for _ in range(n+1)] # 최소값을 찾는 것이 아니므로 무한이 아니라 0 써도 된다고 판단 (0,1로 구분)
answer = 0

for _ in range(m):
    a, b = map(int, input().split()) # 가중치 없으니 1
    graph[a][b] = 1

for k in range(1, n+1):
    for a in range(1, n+1):
        for b in range(1, n+1):
            if graph[a][k] == graph[k][b] == 1: # 양방향이 맞아야함
                graph[a][b] = 1


for i in range(1, n+1):
    check = 0
    for j in range(1, n+1):
        check += graph[i][j] + graph[j][i]
    if check == n-1 :
        answer += 1


print(answer)
