#NO.17087 숨바꼭질 6
import sys
input = sys.stdin.readline

def gcd(x, y):
    while y:
        x, y = y, x%y
    return x
    
n, s = map(int,input().split())
li = list(map(int,input().split()))
dif = list(set(abs(li[i]-s) for i in range(n)))
d = min(dif)
for i in range(len(dif)):
    d = gcd(dif[i],d)

print(d)