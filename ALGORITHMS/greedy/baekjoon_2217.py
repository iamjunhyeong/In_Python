#NO.2217 로프
import sys 
input = sys.stdin.readline

n = int(input())
m = [int(input()) for _ in range(n)]
m.sort()

Max = 0
for i in range(n):
    w = m[i] * (n-i)
    if Max < w:
        Max = w
    
print(Max)