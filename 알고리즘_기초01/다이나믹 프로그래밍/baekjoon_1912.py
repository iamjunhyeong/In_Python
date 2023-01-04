n = int(input())
arr = list(map(int,input().split()))

dp = [0 for _ in range(n)]
dp[0] = arr[0]

for i in range(n-1):
    dp[i] = arr[i]
    for j in range(i+1,n):
        if arr[j] > 0:
            dp[j] = max(dp[j-1]+arr[j],arr[j])
        if dp[j] < 0: break




print(dp[n-1])
