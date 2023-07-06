#경쟁적 전염

# NXN 시험관 , 1X1칸
# 1~K 번까지의 바이러스 종류 중 하나에 속함

# 상하좌우방향으로 바이러스가 증식 -> 번호 낮은 것부터 먼저 증식
# s초 후의 바이러스 종류 출력 없으면 0


# 알고리즘 구상
# 1초 뒤마다 상하좌우 
# 단 , 벽일때 고려 / 숫자 만났을때 고려 
# 어짜피 작은게 무조건 이긴다는거
# 위치를 어떻게 받을지

from collections import deque
 
n, k = map(int, input().split())
virus_list = [] # 전체 시험관
virus_loc = [] # # 바이러스 번호 인덱스에 위치 저장 -> 하려 했는데 인덱스 무지크고그러면 안될거같아서 그냥 다 추가
for i in range(n):
  virus_list.append(list(map(int, input().split())))
  for j in range(n):
    if virus_list[i][j] != 0:
      virus_loc.append(((virus_list[i][j], i, j)))

S, X, Y = map(int, input().split())

# 상하좌우 순서
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
 
def bfs(s, X, Y):
  queue = deque(virus_loc) # 바이러스 순서대로 다 퍼지는 거 확인하기 위해 queue
  count = 0
  while queue:
    if count == s:
      #시간 종료
      break
    for _ in range(len(queue)):
      _num, _x, _y = queue.popleft()
      for i in range(4):
        nx = _x + dx[i]
        ny = _y + dy[i]

        # 벽넘는 조건
        if nx < 0 or nx >= n or ny < 0 or ny >=n:
                continue
        
        #갈 수 있다
        if virus_list[nx][ny] == 0:
          virus_list[nx][ny] = virus_list[_x][_y]
          queue.append((virus_list[nx][ny], nx, ny))
    count += 1
  return virus_list[X-1][Y-1]
 
virus_loc.sort()
print(bfs(S, X, Y))