#NO.11724 연결 요소의 개수
from collections import deque
import sys 
input = sys.stdin.readline

def bfs(i):
    qu = deque()
    qu.append(i)
    visited[i] = 1

    while qu:
        a = qu.popleft()
        for j in graph[a]:
            if visited[j]:
                continue
            qu.append(j)
            visited[j] = 1

n,m = map(int,input().split())
graph = [[] for _ in range(n+1)]
visited = [0] * (n+1)
for i in range(m):
    a, b = map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)

cnt = 0
for i in range(1, n+1):
    if not visited[i]:
        # 연결 요소가 없다면 cnt 추가하고, 방문처리
        if not graph[i]:
            cnt += 1
            visited[i] = 1
        # 연결 요소가 있다면, bfs실행
        else:
            bfs(i)
            cnt += 1
print(cnt)