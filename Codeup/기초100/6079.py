n = int(input())
cnt = 0
sum = 0
for i in range(1, 1001):
    if sum >= n: 
        print(cnt)
        break
    sum += i
    cnt += 1