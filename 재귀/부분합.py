A = list(range(1,13))
AN = len(A)
N = 3
K = 10
arr = [0]*N
sol = []
def func(level, start, S):
    # if sum(arr) > K: return
    if level == N:
        if S == K:
            sol.append(arr.copy())
        return 
    
    for i in range(start, AN-N+level+1):
        arr[level] = A[i]
        if S > K: continue
        func(level+1, i+1, S+A[i])
    
func(0,0,0)
print(len(sol), sol)