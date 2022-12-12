# No.1934 최대공배수
def gcd(x, y):
    if(y==0):
        return x
    else:
        return gcd(y,x%y)
    
for _ in range(int(input())):
    m, n = map(int, input().split())
    print(int(m*n/gcd(m,n)))