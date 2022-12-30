#NO.2193 이친수
import sys
input = sys.stdin.readline
n = int(input())

d = [[0 for _ in range(2)] for _ in range(90+1)]
d[1] = [1, 0]
d[2] = [0, 1]
d[3] = [1, 1]

for i in range(4,n+1):
    d[i][0] = d[i-1][1] 
    d[i][1] = d[i-1][0] + d[i-1][1]

print(sum(d[n]))
