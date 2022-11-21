N = 5
a = list(range(1,N+1))
arr = [0] * N
G = [0]*N
cnt = 0
sol = 0
def func(level):
    global cnt
    global sol
    cnt += 1
    if level == N:
        print(arr)
        sol += 1
        return 

    for i in range(N):
        arr[level] = a[i]
        if arr[level] in G: continue
        else: G[level] = a[i] 
        func(level+1)
        G[level] = 0

func(0)
print(cnt, sol)