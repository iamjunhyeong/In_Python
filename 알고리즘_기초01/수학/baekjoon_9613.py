# NO.9613 GCD 합
from itertools import combinations

def gcd(x, y):
    if y==0:
        return x
    else:
        return gcd(y,x%y)

n = int(input())
li = []
for _ in range(n):
    res = 0
    li = list(map(int,input().split()))
    li = li[::-1]
    li.pop()
    ncr = combinations(li,2)

    for i in ncr:
        res += gcd(i[0],i[1])
    print(res)