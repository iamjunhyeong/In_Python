#NO.7562  나이트의 이동
from collections import deque
import sys
input = sys.stdin.readline

dx = [2, 2,1, 1,-1,-1,-2,-2]
dy = [1,-1,2,-2, 2,-2, 1,-1]

def bfs(sx,sy,ex,ey):
    qu = deque()
    qu.append((sx,sy))
    s[sx][sy] = 1
    
    while qu:
        x,y = qu.popleft()
        if x == ex and y == ey:
            print(s[x][y] - 1)
            return
         
        for i in range(8):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0<=nx<l and 0<=ny<l and s[nx][ny] == 0:
                qu.append((nx,ny))
                # <중요> qu에 넣을때마다 이동횟수이므로 (이전 이동횟수) + 1 해준다.
                s[nx][ny] = s[x][y] + 1  
        
for _ in range(int(input())):
    l = int(input())
    s = [[0] * l for _ in range(l)]
    sx, sy = map(int,input().split())
    ex, ey = map(int,input().split())
    cnt = 0
    bfs(sx,sy,ex,ey)