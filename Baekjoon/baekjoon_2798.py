# NO.2798  블랙잭
def blackjack(li, n, k):
    res = 0
    for i in range(n-2):
        for j in range(i+1,n-1):
            for z in range(j+1,n):
                sum = li[i] + li[j] + li[z]
                if sum <= k and sum > res:
                    res = sum
    return res

n, k = map(int,input().split())
li = list(map(int,input().split()))

print(blackjack(li,n,k))
