#NO.1068 트리
from collections import deque
import sys 
input = sys.stdin.readline

n = int(input())
li = list(map(int,input().split()))
graph = [[] for _ in range(n)]
d = int(input())
cnt = 0

for i in range(n):
    if li[i] == -1:
        continue
    graph[li[i]].append(i)

def bfs(d):
    global cnt
    qu = deque()
    qu.append(d)
    # 잔여 트리 빼기
    for i in range(n):
        if d in graph[i]:
            graph[i].remove(d)
    while qu:
        # 삭제 트리와 그 밑에 트리들 없애기
        x = qu.popleft()
        cnt += 1
        for i in graph[x]:
            qu.append(i)
        # 트리 초기화
        graph[x] = []

bfs(d)
s = 0
for i in range(n):
    if graph[i]:
        continue
    s += 1
print(s-cnt)