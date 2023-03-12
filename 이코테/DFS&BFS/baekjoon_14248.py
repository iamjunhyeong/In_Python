#NO.14248 점프 점프
from collections import deque
import sys 
input = sys.stdin.readline

n = int(input())
stones = [0] + list(map(int,input().split()))
s = int(input())
visited = [0] * (n+1)

def bfs(s): 
    qu = deque()
    qu.append(s)
    visited[s] = 1
    cnt = 1

    while qu:
        x = qu.popleft()
        # 좌우
        for sign in [1,-1]:
            dx = x+(sign*stones[x])
            if 1 <= dx <= n and not visited[dx]:
                visited[dx] = 1
                qu.append(dx)
                cnt += 1
    return cnt

print(bfs(s))