# 트리의 부모 찾기

# 6 : 21

# <-문제->
# 루트 없는 트리 주어짐
# 트리 루트 = 1일때 각 노드의 부모 구하시오

# 첫번째 노드로 1이 들어갔어
# 그러면은 트리브이에는 첨에 i = 4 v=1

import sys
sys.setrecursionlimit(10**6) # 런타임에러 나서 추가
input = sys.stdin.readline

def dfs(tree, v, visited):
	# 현재 노드를 방문 처리
    # 현재 노드와 연결된 다른 노드를 재귀적으로 방문
    for i in tree[v]:
    	if visited[i]==0:
            visited[i] = v
            dfs(tree, i, visited)  

n = int(input())
answer = []

tree = [[] for i in range(n+1)]

for i in range(n-1):
    a,b = map(int,input().strip().split())
     # 2차원 배열 선언
    tree[a].append(b) # 각 인덱스에 연결된 값이 저장되도록
    tree[b].append(a) 

visited = [0]*(n+1)
    
# dfs
dfs(tree,1,visited)

for i in range(2,n+1):
    print(visited[i])

    
