#NO.18352 특정 거리의 도시 찾기
from collections import deque
import sys 
input = sys.stdin.readline

n,m,k,x = map(int,input().split())
graph = [[] for _ in range(n+1)]
v = [300001] * (n+1)
for _ in range(m):
    a,b = map(int,input().split())
    #단방향이다
    graph[a].append(b)

def bfs(s):
    qu = deque()
    qu.append(s)
    v[s] = 0

    while qu:
        x = qu.popleft()

        for i in graph[x]:
            # 최단거리이면 업데이트 후 큐에 추가
            if v[i] > v[x] + 1:
                v[i] = v[x] + 1
                qu.append(i)

bfs(x)
nothing = True
for i in range(1,n+1):
    if v[i] == k:
        print(i)
        nothing = False
if nothing:
    print(-1)

