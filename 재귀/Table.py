max_n = 10
n = 100
k = 2
memo = {}

def func(N, i):
    key = str([N, i])
    if key in memo:
        return memo[key]
        
    if N == 0:
        return 1
    elif N < 0:
        return 0

    cnt = 0
    for j in range(i, max_n+1):
        cnt += func(N-j,j)
    memo[key] = cnt
    
    return cnt

print(func(n, k))

    