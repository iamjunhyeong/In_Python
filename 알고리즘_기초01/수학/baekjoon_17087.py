import sys
input = sys.stdin.readline

def gcd(x, y):
    if y==0:
        return x
    else:
        return gcd(y,x%y)

n, s = map(int,input().split())
li = list(map(int,input().split()))
dif = list(set(abs(li[i]-s) for i in range(n)))
d = min(dif)
for i in range(len(dif)):
    d = gcd(dif[i],d)

print(d)