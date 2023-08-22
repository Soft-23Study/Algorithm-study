# Edited by Seungho Song

'''
서로소 집합
: 서로소 부분집합들로 나누어진 원소들의 데이터를 처리하기 위한 자료구조
-> union & find로 조작할 수 있다.

* find : 어떤 원소가 주어졌을 때, 이 원소의 루트노드를 반환하는 연산
루트노드가 서로 다른 두 원소는 서로소 관계에 있다.
'''

# makeset
n, e = 6, 4 # n: 노드 개수 e: 간선 개수
parent = [0]*(n+1)
for i in range(1, n+1):
    # 초기 세팅은 자기 자신이 부모
    parent[i] = i

# find
def find(x):
    if x==parent[x]:
        return x
    return find(parent[x])

def find_compression(x):
    if x != parent[x]:
        parent[x] = find(parent[x])
    return parent[x]
# union
def union(a, b):
    a = find(a)
    b = find(b)
    # 편의상 루트 노드가 큰 집합이 작은 집합으로 들어가게끔
    if a<b:
        parent[b] = a
    else:
        parent[a] = b

for i in range(e):
    a, b = map(int, input().split())
    union(a, b)

print('각 원소가 속한 집합: ', end=' ')
for i in range(1, n+1):
    print(find(i), end=' ')

print()
print('부모 테이블: ', end=' ')
for i in range(1, n+1):
    print(parent[i], end=' ')

# 시간 복잡도 : O(V + M(1 + log(2-M/V)V))

# 사이클 판별 : 계속 union을 수행하면서, 부모 노드가 같은 두 원소가 있으면 사이클이다.
cycle = False
for i in range(e):
    a, b = map(int, input().split())
    if find(a) == find(b):
        cycle = True
        break
    else:
        union(a, b)
if cycle: print('cycle exist')
else: print('there\'s no cycle')

# 크루스칼 알고리즘
edges = []
result = 0

for _ in range(e):
    a, b, cost = map(int, input().split())
    edges.append((cost, a, b))

edges.sort() #항상 정렬을 시켜준다.

for edge in edges:
    cost, a, b = edge
    if find(a) != find(b): # 사이클이 아닐 때
        union(a, b)
        result += cost
# 시간복잡도 : O(ElogE) <- sorting 할 때 젤오래걸린다.