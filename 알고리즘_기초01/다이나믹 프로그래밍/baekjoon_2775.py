#NO.2775 부녀회장이 될테야
for _ in range(int(input())):
    k = int(input())
    n = int(input())
    
    dp = [[0 for _ in range(n+1)] for _ in range(k+1)]
    for i in range(n+1):
        dp[0][i] = i
    
    for i in range(1,k+1):
        for j in range(1,n+1):
            for z in range(1,j+1):
                dp[i][j] += dp[i-1][z]
    
    print(dp[k][n])
