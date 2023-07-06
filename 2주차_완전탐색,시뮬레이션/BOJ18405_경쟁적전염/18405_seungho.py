import sys
from collections import deque

input = sys.stdin.readline

n, k = map(int, input().strip().split())
arr = [[-1]*(n+1) for _ in range(n+1)] #n+1 * n+1 크기의 맵

queue = deque([])

for i in range(1, n+1):
    temp = list(map(int, input().strip().split()))
    for j in range(1, n+1):
        arr[i][j] = temp[j-1]
        if temp[j-1] > 0:
            queue.append

s, x, y = map(int, input().strip().split())

dy = [-1,1,0,0] #상, 하, 좌, 우
dx = [0,0,-1,1]



for sec in range(1, s+1):
    for virus in range(1, k+1):
