'''
복잡한 문제를 풀 때 나오는 기본적인 실수들을 조심해야겠다.

1. DFS 함수를 짤 때, 재귀를 들어가는 로직에서 방문처리 여부를 필터링하지 않아 에러
2. y, x에 대한 방향정립을 일관적이게 하지 않아 나온 에러
3. 변수 초기화를 반복문 전에 해버려서 나온 에러 (day_united)
+ 문제 로직에 대한 로직 이해 부족으로 나온 에러
-> 모든 dfs를 돌 때, 기본적으로 한 개의 국가가 temp_united에 포함될 것이므로,
4. day_united 포함여부를 따질 때 temp_united가 2 이상일 때로 넣었어야 한다. 1로 해서 에러

4번은 충분히 나올수 있는 에러였지만, 1,2,3번 에러는 기본 부족인것 같다.
복잡한 문제를 짤 때, 기본적인 코드들은 잔실수없이 풀어낼 때까지 노력해야겠다.
'''


import sys

input = sys.stdin. readline
sys.setrecursionlimit(2500)

n, l, r = map(int ,input().strip().split())
earth = [[-1]*(n+1) for _ in range(n+1)]
visited = [[False] * (n+1) for _ in range(n+1)]

for i in range(1, n+1):
    temp = list(map(int, input().strip().split()))
    for j in range(1, n+1):
        earth[i][j] = temp[j-1]

dy = [-1,1,0,0]
dx = [0,0,-1,1]



def dfs(graph, y, x, visited, temp_united):
    visited[y][x] = True
    temp_united.append((y,x))
    for i in range(4):
        ny, nx = y + dy[i], x + dx[i]
        if nx<=0 or nx>n or ny<=0 or ny>n:
            continue
        if not visited[ny][nx] and l <= abs(graph[ny][nx] - graph[y][x]) <= r:
            #append
            dfs(graph, ny, nx, visited, temp_united)


day = 0
while True:
    visited = [[False]*(n+1) for _ in range(n+1)]
    temp_united = []
    day_united = []
    for i in range(1, n+1):
        for j in range(1, n+1):
            if not visited[i][j]:
                temp_united = []
                dfs(earth, i, j, visited, temp_united)
                if len(temp_united)>1:
                    day_united.append(temp_united)
    if len(day_united)==0:
        break
    for nations in day_united:
        united_sum = 0
        for k in range(len(nations)):
            united_sum += earth[nations[k][0]][nations[k][1]]
        united_sum //= len(nations)
        for k in range(len(nations)):
            earth[nations[k][0]][nations[k][1]] = united_sum
    day += 1

print(day)