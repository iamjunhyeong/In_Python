n, k = map(int,input().split())
a = list(map(int,input().split()))
b = list(map(int,input().split()))

for _ in range(k):
    i = a.index(min(a))
    j = b.index(max(b))

    a[i], b[j] = b[j], a[i]

print(sum(a))

