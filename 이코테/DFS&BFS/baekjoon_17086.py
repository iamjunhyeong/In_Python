#NO.17086 아기상어2
from collections import deque
import sys 
input = sys.stdin.readline

n, m = map(int,input().split())
s = [list(map(int,input().split())) for _ in range(n)]
qu = deque()

dx = [1,-1,0,0,1,-1,1,-1]
dy = [0,0,1,-1,1,-1,-1,1]

# 상어가 있는 인덱스를 qu에 담는다.
for i in range(n):
    for j in range(m):
        if s[i][j] == 1:
            qu.append((i,j)) 
            
def bfs(qu):
    # 미리 상어 위치를 큐에 담아놔서 먼저빠짐
    while qu:
        x,y = qu.popleft()

        for i in range(8):
            nx = dx[i] + x
            ny = dy[i] + y
            if 0<=nx<n and 0<=ny<m and s[nx][ny] == 0:
                qu.append((nx,ny))
                # 배열에 상어부터의 거리 입력
                s[nx][ny] = s[x][y] + 1

bfs(qu)
#최댓값찾기
maxx = 0
for i in range(n):
    maxx = max(*s[i],maxx)
print(maxx-1)