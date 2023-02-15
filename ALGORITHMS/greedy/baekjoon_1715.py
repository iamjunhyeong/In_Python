#NO.1715 카드정렬하기
import heapq
import sys 
input = sys.stdin.readline

n = int(input())
li = []
# heapq으로 입력받기
for _ in range(n):
    num = int(input())
    heapq.heappush(li, num)
res = 0

while len(li) > 1:
    # 최솟값 하나씩 빼고 더함
    a = heapq.heappop(li)
    b = heapq.heappop(li)
    res += a+b
    heapq.heappush(li,a+b)
    
print(res)