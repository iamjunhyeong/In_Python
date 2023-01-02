#NO.14002 가장 긴 증가하는 부분수열4
import sys
input = sys.stdin.readline

n = int(input())
array = list(map(int,input().split()))
dp = [1]*n
box = []

for i in range(n) :
    for j in range(i) :
        if array[i] > array[j] :
            dp[i] = max(dp[i],dp[j]+1)

chk = max(dp)
print(chk)

for i in range(n - 1, -1 ,-1):
    if dp[i] == chk:
        box.append(array[i])
        chk -= 1
box.reverse()
print(*box)