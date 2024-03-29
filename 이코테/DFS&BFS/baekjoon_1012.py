#NO.1012 ? κΈ°λ λ°°μΆ
from collections import deque
import sys
input = sys.stdin.readline

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
    
def bfs(graph,x,y):
    qu = deque()
    qu.append((x,y))
    graph[x][y] = 0
    
    while qu:
        x,y = qu.popleft()
        for i in range(4):
            nx = dx[i] + x
            ny = dy[i] + y
            if nx < 0 or nx >=n or ny < 0 or ny >= m:
                continue
            if graph[nx][ny] == 1:
                #?΄κ±? ??ΌκΈ? ?λ¬Έμ λ°©λ¬Έ??κ³³μ κ³μ ?€? €? ?κ°μ΄κ³Όλ¨
                graph[nx][ny] = 0
                qu.append((nx,ny))

for _ in range(int(input())):
    n,m,k = map(int,input().split())
    graph = [[0] * m for _ in range(n)]
    for i in range(k):
        a,b = map(int,input().split())
        graph[a][b] = 1

    cnt = 0
    for i in range(n):
        for j in range(m):
            # λ°°μΆκ°? ?? κ³³λ§ ?€?΄κ°?
            if graph[i][j] == 1:
                bfs(graph,i,j)
                cnt += 1
    print(cnt)