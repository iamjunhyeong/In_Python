# NO.5547 일루미네이션
# 풀이참고 : https://reliablecho-programming.tistory.com/110
from collections import deque
import sys 
input = sys.stdin.readline

col, row = map(int, input().split())

board = [[0 for _ in range(col+2)] for _ in range(row+2)]
visited = list(list(0 for _ in range(col+2)) for _ in range(row+2))
for i in range(1, row+1):
    board[i][1:col+1] = map(int, input().split())

dx = [1, 1, 0, 0, -1, -1]
dy = [[-1, 0, 1, -1, -1, 0], [0, 1, 1, -1, 0, 1]]



def bfs(i,j):
    qu = deque()
    qu.append([i,j])
    visited[i][j] = 1
    cnt = 0
    while (qu):
        x, y = qu.popleft()

        for i in range(6):
            nx = x + dx[i]
            ny = y + dy[x%2][i]
            if  0 <= nx < row+2 and 0 <= ny < col+2:
                if (board[nx][ny]==0 and not visited[nx][ny]):
                    qu.append([nx,ny])
                    visited[nx][ny] = 1
                elif board[nx][ny] == 1:
                    cnt += 1
    return (cnt)

print(bfs(0,0))