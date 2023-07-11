import sys

inpujt = sys.stdin.readline

n, m, x, y, k= map(int, input().strip().split())
arr = []
for _ in range(n):
    arr.append(list(map(int,input().split())))

directions = list(map(int,input().split()))

# 생각 갈아엎음
# 전에는 초기값으로부터 방향을 위아래 / 좌우로 증감시켜주는 벡터를 설정하려 했으나,
# 매 순간순간마다의 주사위 값을 update 해줘야겠다는 생각으로 전환하고 다시 풀듯...