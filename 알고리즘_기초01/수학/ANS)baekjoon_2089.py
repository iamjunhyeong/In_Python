#NO.2089 -2진수
n = int(input())
if n == 0:
    print(0)
else:
    ans = ''
    while n:
        ans += str(n%2)
        n//=2
        n*=-1
    print(ans[::-1])
