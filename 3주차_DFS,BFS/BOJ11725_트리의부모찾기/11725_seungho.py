'''
처음 입력 데이터 저장 방식을 인접 행렬 vs 인접 그래프 중에서 고민함.
인접 행렬로 하자니 N*N = N^2의 메모리를 잡아먹어서 지양.
인접 리스트를 통해 DFS로 풀자는 생각으로 풀었다.
'''

import sys

input = sys.stdin.readline

n = int(input().strip())
sys.setrecursionlimit(110000)

graph = [[]*(n+1) for _ in range(n+1)] #인접 그래프 초기화
visited = [False] * (n+1)
visited[1] = True
answer = [0]*(n+1)
def dfs(graph, start, visited, head):
    visited[start] = True
    answer[start] = head

    for node in graph[start]:
        if not visited[node]:
            dfs(graph, node, visited, start)


for i in range(n-1):
    x, y = map(int, input().strip().split())
    if x not in graph[y]:
        graph[y].append(x)
    if y not in graph[x]:
        graph[x].append(y)


dfs(graph, 1, visited, 0)

for a in answer[2:]:
    print(a)