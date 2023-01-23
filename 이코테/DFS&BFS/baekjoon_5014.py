#NO.5014    스타트링크
from collections import deque
import sys 
input = sys.stdin.readline

f,s,g,u,d = map(int,input().split())
t = [0] * (f+1)
t[s] = 1

def bfs():
    q = deque()
    q.append(s)

    while q:
        if t[g]: 
            print(t[g]-1)
            break

        x = q.popleft()
        for dx in x+u, x-d:
            if 1 <= dx <= f and not t[dx]:
                t[dx] = t[x] + 1
                q.append(dx)
    else:
        print("use the stairs")

bfs()