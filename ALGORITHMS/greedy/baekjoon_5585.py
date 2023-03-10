#NO.5585 거스름돈
n = 1000 - int(input())
cnt = 0
while n:
    if n >= 500:
        n -= 500
        cnt += 1
    elif n >= 100:
        n -= 100
        cnt += 1
    elif n >= 50:
        n -= 50
        cnt += 1
    elif n >=10:
        n -= 10
        cnt += 1
    elif n >= 5:
        n -= 5
        cnt += 1
    elif n >= 1:
        n -= 1
        cnt += 1
print(cnt)