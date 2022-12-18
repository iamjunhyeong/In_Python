n = int(input())

sum = 0
for h in range(n+1):
    if h == 3:
        sum += 3600
    else:
        sum += 1575
print(sum)