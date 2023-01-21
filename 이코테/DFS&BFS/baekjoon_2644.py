#NO.2644 촌수계산
from collections import deque

n = int(input())
a,b = map(int,input().split())
m = int(input())

graph = [[] for _ in range(n+1)]
for i in range(m):
    x,y = map(int,input().split())
    graph[x].append(y)
    graph[y].append(x)

visited = [0] * (n+1)

def bfs(s):
    queue = deque()
    queue.append((s,0))

    while queue:
        node, d = queue.popleft()
        visited[node] = d
        for i in graph[node]:
            if visited[i] == 0:
                queue.append((i, d+1))

bfs(a)
print(visited[b] if visited[b] != 0 else -1)