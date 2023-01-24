#NO.2468 안전영역
from collections import deque

n = int(input())
graph = []
MAX = 0
for i in range(n):
    graph.append(list(map(int,input().split())))
    for j in range(n):
        if graph[i][j] > MAX:
            MAX = graph[i][j]
dx = [1,-1,0,0]
dy = [0,0,1,-1]

def bfs(x,y,h):
    q = deque()
    q.append((x,y))
    visited[x][y] = 1

    while q:
        x, y = q.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < n and 0 <= ny < n:
                if graph[nx][ny] > h and visited[nx][ny] == 0:
                    q.append((nx,ny))
                    visited[nx][ny] = 1


res = [0] * (MAX+1)
for k in range(MAX+1):
    visited = [[0] * (n+1) for _ in range(n+1)]
    for i in range(n):
        for j in range(n):
            if graph[i][j] > k and visited[i][j] == 0:
                bfs(i,j,k)
                res[k] += 1

print(max(res))