#NO.12761 돌다리
from collections import deque
import sys
input = sys.stdin.readline

def bfs(a,b,s,e):
    qu = deque()
    qu.append(s)
    v[s] = 0

    while qu:
        x = qu.popleft()
        if x == e:
            break
       
       # 8가지 방법 모두 적용해보기 
       # 최솟값 변동이 없다면 그 루트는 버리기 
        for sign in [1,-1]:
            if 0<= x+sign < MAX and v[x] + 1 < v[x+sign]:
                qu.append((x+sign))
                v[x+sign] = v[x] + 1
            for i in a,b:
                if 0 <= x+(sign*i) < MAX and v[x] + 1 < v[x+(sign*i)]:
                    qu.append((x+(sign*i)))
                    v[x+(sign*i)] = v[x] + 1
                    
                if 0 <= x*i < MAX and v[x] + 1 < v[x*i]:
                    qu.append((x*i))
                    v[x*i] = v[x] + 1

MAX = 100001
a,b,n,m = map(int,input().split()) 
v = [MAX for _ in range(MAX)]
sign = 1
bfs(a,b,n,m)
print(v[m])