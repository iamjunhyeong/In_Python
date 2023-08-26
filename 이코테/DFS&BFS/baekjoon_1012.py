#NO.1012 ?��기농 배추
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
                #?���? ?��?���? ?��문에 방문?��?��곳을 계속 ?��?��?�� ?��간초과남
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
            # 배추�? ?��?�� 곳만 ?��?���?
            if graph[i][j] == 1:
                bfs(graph,i,j)
                cnt += 1
    print(cnt)