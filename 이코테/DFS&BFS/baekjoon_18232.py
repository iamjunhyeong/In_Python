#NO.18232 텔레포트 정거장
from collections import deque
import sys 
input = sys.stdin.readline

n, m = map(int,input().split())
s, e = map(int,input().split())
graph = [[] for _ in range(n+1)]
for i in range(m):
    a,b = map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)
# 걸리는 시간 최댓값으로 초기화
v = [300001] * (n+1)

def bfs(s,e):
    qu = deque()
    qu.append(s)
    v[s] = 0

    while qu:
        x = qu.popleft()
        if x == e:
             return 
        # 현재까지 나온 시간 중 최솟값일때 대입
        if 1<=x+1<=n and v[x]+1 < v[x+1]:
            qu.append(x+1)
            v[x+1] = v[x] + 1
        if 1<=x-1<=n and v[x]+1 < v[x-1]:
            qu.append(x-1) 
            v[x-1] = v[x] + 1 
        for i in graph[x]:
            if v[x] + 1 < v[i]:
                v[i] = v[x] + 1
                qu.append(i)
bfs(s,e)
print(v[e])
            