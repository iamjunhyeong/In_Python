#NO.2606 바이러스
from collections import deque

n = int(input())
m = int(input())
cnt = 0
graph = [[] for _ in range(n+1)]
visited = [False] * 101
for _ in range(m):
    a,b = map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)

def bfs(s):
    global cnt
    queue = deque()
    queue.append(s)
    visited[s] = True
    while queue:
        for i in graph[queue.popleft()]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True  
                cnt += 1
bfs(1)
print(cnt)