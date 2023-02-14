#NO.1715 카드정렬하기
import heapq
import sys 
input = sys.stdin.readline

n = int(input())
li = []
for _ in range(n):
    num = int(input())
    heapq.heappush(li, num)
res = 0

while len(li) > 1:
    a = heapq.heappop(li)
    b = heapq.heappop(li)
    res += a+b
    heapq.heappush(li,a+b)
    
print(res)