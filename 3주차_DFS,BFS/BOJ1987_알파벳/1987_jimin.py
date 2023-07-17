# ---------------------------------------------------- 1트 => 시간초과
# import sys
# sys.setrecursionlimit(10**6)

# r,c = map(int,input().split())
# _map = []
# for _ in range(r): _map.append(list(input()))

# dx = [-1,0,1,0]
# dy = [0,-1,0,1]

# def dfs(cur_x,cur_y):
#     global answer

#     path.append(_map[cur_x][cur_y])

#     for i in range(4):
#         next_x, next_y = cur_x + dx[i], cur_y + dy[i]

#         if next_x<0 or next_x>=r or next_y<0 or next_y>=c: continue
#         if _map[next_x][next_y] in path: continue

#         dfs(next_x,next_y)
    
#     answer = max(len(path),answer)
#     path.pop()
   
# path = []
# answer = 0

# dfs(0,0)

# print(answer)

# ---------------------------------------------------- 2트
# 1. 1트에서는 방문한 알파벳들을 path 배열에 저장해서 확인했음 => in 키워드로 매번 path 검색 시 시간 많이 소요
# 2. 2트에서 path 배열 대신, 알파벳들에 대해 방문이 되었냐/아니냐 를 마킹하는 visited_alpha 배열 생성
# ---------------------------------------------------- 
r,c = map(int,input().split())
_map = []
for _ in range(r): _map.append(list(input()))

dx = [-1,0,1,0]
dy = [0,-1,0,1]

visited_alpha = [0] * 26

def dfs(cur_x,cur_y,cnt):
    global answer

    for i in range(4):
        next_x, next_y = cur_x + dx[i], cur_y + dy[i]

        if next_x<0 or next_x>=r or next_y<0 or next_y>=c: continue
        if visited_alpha[ord(_map[next_x][next_y])-ord('A')] == 1: continue

        visited_alpha[ord(_map[next_x][next_y])-ord('A')] = 1
        dfs(next_x,next_y,cnt+1)
        visited_alpha[ord(_map[next_x][next_y])-ord('A')] = 0
    
    answer = max(cnt,answer)
    
answer = 0

visited_alpha[ord(_map[0][0])-ord('A')] = 1
dfs(0,0,1)

print(answer)