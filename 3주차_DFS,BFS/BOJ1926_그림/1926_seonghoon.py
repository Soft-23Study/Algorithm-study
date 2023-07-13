
##### recursion으로 풀면 recursion runtime error가 나므로 DFS로 풀고싶으면 스택을 써야한다 #####


x = 0; y = 0
dx = [1, -1, 0, 0] # 동 서 남 북
dy = [0, 0, -1, 1] # 동 서 남 북

count = 0
max_area = 0

n, m = map(int, input().split())

painting = [] # 2차원 배열을 저장

for _ in range(n):
    row = list(map(int, input().split()))
    painting.append(row)

# 해당 (X,Y) 좌표를 1 -> 2로 바꾸고, 동서남북을 체크하여 재귀적으로 실행하는 재귀함수
def calculateArea(y, x, area):

    painting[y][x] = 2 ## 이미 살펴본 곳은 2로 할당

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if nx >= m or nx < 0 or ny >= n or ny < 0:
            continue

        if painting[ny][nx] == 1:
            area += 1
            area = calculateArea(ny, nx, area)

    return area

for y in range(n):
    for x in range(m):
        if painting[y][x] == 1:
            count += 1 # calculateArea를 첫 실행하는 경우, 그림이기 때문에 count를 1 증가시킴
            area = calculateArea(y, x, 1)
            max_area = max(max_area, area)

print(count)
print(max_area)

