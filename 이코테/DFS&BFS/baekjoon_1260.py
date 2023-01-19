#NO.1260 DFS와 BFS
from collections import deque
import sys 
input = sys.stdin.readline

n, m, v = map(int,input().split())
arr = []
graph = [[] for _ in range(n+1)]
visited_d = [False] * 1001
visited_b = [False] * 1001
for _ in range(m):
    arr.append(list(map(int,input().split())))

for i,j in arr:
    graph[i].append(j)
    graph[j].append(i)

def dfs(graph, v, visited_d):
    visited_d[v] = True
    print(v, end=' ')
    for i in sorted(graph[v]):
        if not visited_d[i]:
            dfs(graph, i, visited_d)

def bfs(graph, v, visited_b):
    queue = deque([v])
    visited_b[v] = True
    
    while queue:
        q = queue.popleft()
        print(q, end=' ')
        for i in sorted(graph[q]):
            if not visited_b[i]:
                queue.append(i)
                visited_b[i] = True

dfs(graph, v, visited_d)
print()
bfs(graph, v, visited_b)