#NO.13565 침투
from collections import deque
import sys 
input = sys.stdin.readline

n, m = map(int,input().split())
graph = [list(map(int,input().strip())) for _ in range(n)]
v = [[0]*m for _ in range(n)]
dx = [1,-1,0,0]
dy = [0,0,1,-1]

def bfs(i,j):
    qu = deque()
    qu.append((i,j))
    v[i][j] = 1
    
    while qu:
        x,y = qu.popleft()
        if x == n-1:
            return True
        for i in range(4):
            nx = dx[i] + x
            ny = dy[i] + y
            if 0<=nx<n and 0<=ny<m and not v[nx][ny] and graph[nx][ny] == 0:
                qu.append((nx,ny))
                v[nx][ny] = 1
    return False

# 아웃사이드 쪽에서 공급되므로 첫번째행만 반복문돌림
for j in range(m):
    if graph[0][j] == 0 and not v[0][j]:
        # 인사이드까지 침투되었다면 True를 리턴하므로 YES출력 후 중단
        if bfs(0,j):
            print("YES")
            break
else:    
    print("NO")