A = list(input().split())
N = len(A)
K = N
arr = [0] * N
def func(level, S):
    if level == K:
        print(arr)
        return
    
    for i in range(S, N):
        arr[level] = A[i]
        func(level+1, i)

func(0,0)