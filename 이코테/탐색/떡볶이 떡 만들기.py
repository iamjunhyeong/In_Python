#순차탐색 
n, m = map(int, input().split())
rices = list(map(int,input().split()))
cutline = max(rices)
res = []

while cutline >= 0:
    sum = 0
    for rice in rices:
        if cutline <= rice:
            sum += rice - cutline
    if sum == m:
        res.append(cutline)
    cutline -= 1

print(max(res))

#이진탐색
n, m = map(int, input().split())
rices = list(map(int,input().split()))

start = 0
end = max(rices)

res = 0
while start <= end:
    total = 0
    mid = (start + end) // 2
    for x in rices:
        if x > mid:
            total += x - mid
    if total < m:
        end = mid - 1
    else:
        res = mid 
        start = mid + 1

print(res)