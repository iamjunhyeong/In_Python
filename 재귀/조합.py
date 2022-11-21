N = 5
K = 3
A = list(range(N))
arr = [0] * K
def func(level, S):
    if level == K: 
        print(arr)
        return
    
    for i in range(S, N-K+level+1):
        arr[level] = A[i]
        func(level+1, i+1)

func(0,0)