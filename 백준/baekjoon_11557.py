#NO.11557 Yangjojang of The Year
for _ in range(int(input())):
    n = int(input())
    m = 0
    u = ''
    for i in range(n):
        a, b = input().split()
        if int(b) > m:
            m = int(b)
            u = a
    print(u)