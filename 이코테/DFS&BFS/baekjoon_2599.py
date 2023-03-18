#NO.2599 짝정하기
#참고 : https://settembre.tistory.com/73
import sys 
input = sys.stdin.readline

n = int(input())
graph = []
couple = [[] for _ in range(3)]
for i in range(3):
    m, g = map(int,input().split())
    graph.append(m)
    graph.append(g)

for i in range(graph[0]+1):
    a = i
    d = graph[0] - a
    e = graph[5] - d
    b = graph[2] - e
    c = graph[1] - b
    f = graph[4] - c
    if a>=0 and b>=0 and c>=0 and d>=0 and e>=0 and f>=0:
        print(1)
        print(a,d)
        print(b,e)
        print(c,f)
        break
else:
    print(0)
        