n, m = map(int, input().split())
cash = []

for _ in range(n):
    cash.append(int(input()))

d =  [10001] * (m+1)

d[0] = 0
for i in range(n):
    for j in range(cash[i], m+1):
        if d[j-cash[i]] != 10001:
            d[j] = min(d[j], d[j-cash[i]]+1)

if d[m] == 10001:
    print(-1)
else:
    print(d[m])
