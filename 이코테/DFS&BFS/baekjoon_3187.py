#NO.3187 양치기 꿍
#백준 3184와 흡사
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
    v = 0
    k = 0
    visited[a][b] = 1

    while qu:
        x, y = qu.popleft()
        if graph[x][y] == 'v':
            v += 1
        elif graph[x][y] == 'k':
            k += 1

        for i in range(4):
            nx = dx[i] + x
            ny = dy[i] + y
            if 0<=nx<r and 0<=ny<c:
                if visited[nx][ny]:
                    continue
                if graph[nx][ny] != '#':
                    qu.append((nx,ny))
                visited[nx][ny] = 1
    return v, k

total_k = 0
total_v = 0
for i in range(r):
    for j in range(c):
        v = 0
        k = 0
        if graph[i][j] != '#' and not visited[i][j]:
            v,k = bfs(i,j)
            if v < k:
                total_k += k
            else:
                total_v += v
print(total_k, total_v)

