def Merge(a):
    n = len(a)
    if n <= 1:
        return a
    mid = n//2
    left = a[:mid]
    right = a[mid:]
    Merge(left)
    Merge(right)
    i = 0
    j = 0
    ia = 0
    result = []
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            a[ia] = left[i]
            ia += 1
            i += 1
        else:
            a[ia] = right[j]
            ia += 1
            j += 1

    while i < len(left):
        a[ia] = left[i]
        ia += 1
        i += 1
    while j < len(right):
        a[ia] = right[j]
        ia += 1
        j += 1

d = [6,8,3,9,10,1,2,4,7,5]
Merge(d)
print(d)