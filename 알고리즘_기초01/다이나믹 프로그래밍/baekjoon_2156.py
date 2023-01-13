#NO. 2156 포도주
import sys
input = sys.stdin.readline

n = int(input())
arr = [0] + [int(input()) for _ in range(n)]
dp = [0 for i in range(n+1)]
dp[0] = arr[0]
dp[1] = arr[1]
for i in range(2,n+1):
    dp[i] = max(dp[i-1], dp[i-3]+arr[i-1]+arr[i],dp[i-2]+arr[i])

print(dp[n])