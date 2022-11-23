# No.7568 덩치 비교.
n = int(input())
li = []
for _ in range(n):
    li.append(list(map(int,input().split())))

rank = [1] * n
for i in range(n):
    for j in range(n):
        if i == j: continue
        if li[i][0] > li[j][0] and li[i][1] > li[j][1]:
            rank[j] += 1

print(*rank, sep=" ")