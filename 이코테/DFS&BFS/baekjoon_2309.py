#NO.2309 일곱 난쟁이
arr = []
for _ in range(9):
    arr.append(int(input()))

for i in range(9-1):
    for j in range(i+1,9):
        res = sum(arr) - arr[i] - arr[j]
        if res == 100:
            a, b = arr[i], arr[j]
            break
arr.remove(a)
arr.remove(b)

for i in sorted(arr):
    print(i)