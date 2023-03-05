#NO.3184 양
from collections import deque
import sys
input = sys.stdin.readline

r, c = map(int,input().split())
graph = [list(input()) for _ in range(r)]
visited = [[0] * c for _ in range(r)]

dx = [1,-1,0,0]
dy = [0,0,1,-1]

def bfs(a,b):
    qu = deque()
    qu.append((a,b))
    v = 0   # 늑대
    o = 0   # 양
    visited[a][b] = 1

    while qu:
        x, y = qu.popleft()
        # 해당 자리가 양이면 o += 1 늑대이면 v += 1
        if graph[x][y] == 'v':
            v += 1
        elif graph[x][y] == 'o':
            o += 1

        for i in range(4):
            nx = dx[i] + x
            ny = dy[i] + y
            if 0<=nx<r and 0<=ny<c:
                if visited[nx][ny]:
                    continue
                if graph[nx][ny] != '#':
                    qu.append((nx,ny))
                visited[nx][ny] = 1
    return v, o

total_o = 0
total_v = 0
for i in range(r):
    for j in range(c):
        v = 0
        o = 0
        # 울타리가 아니거나 방문한곳이 아니라면 실행
        if graph[i][j] != '#' and not visited[i][j]:
            v,o = bfs(i,j)
            # 양이 늑대보다 많다면 전체 양의 수만 추가
            if v < o:
                total_o += o
            # 그렇지 않으면 전체 늑대 수만 추가
            else:
                total_v += v
print(total_o, total_v)

