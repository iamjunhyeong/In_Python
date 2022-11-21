def func(level):
    if len(level) == 1:
        return level
    
    mid = (len(level)+1) // 2

    left = func(level[:mid])
    right = func(level[mid:])

    i,j = 0, 0
    level2 = []
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            level2.append(left[i])
            arr.append(left[i])
            i += 1
        else:
            level2.append(right[j])
            arr.append(right[j])
            j += 1
    while i < len(left):
        level2.append(left[i])
        arr.append(left[i])
        i += 1
    while j < len(right):
        level2.append(right[j])
        arr.append(right[j])
        j += 1

    return level2

N, K = map(int,input().split())
li = list(map(int, input().split()))
arr = []
func(li)
if len(arr) >= K:
    print(arr[K-1])
else:
    print(-1)
