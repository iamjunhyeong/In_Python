#NO.13398 연속합2
n = int(input())
arr = list(map(int,input().split()))
dp = [[-1000]*n for _ in range(2)]

ans = -1000
for i in range(n):
    dp[0][i] = max(dp[0][i-1] + arr[i], arr[i])
    dp[1][i] = max(dp[0][i-1], dp[1][i-1]+arr[i])
    ans = max(ans, dp[0][i], dp[1][i])

print(ans)