#NO.14562 태권왕
#참고: https://dreamtreeits.tistory.com/142
from collections import deque
import sys 
input = sys.stdin.readline

def bfs(a,b):
    qu = deque()
    qu.append((a,b,0))

    while qu:
        a,b,t = qu.popleft()

        if a == b:
            return t
        if b+3 >= 2*a:
            if v[a*2] == -1:
                qu.append((2*a,b+3,t+1))
        if v[a+1] == -1:
            qu.append((a+1,b,t+1))
            
for _ in range(int(input())):
    a,b = map(int,input().split())
    v = [-1] * 10000
    print(bfs(a,b))