def search(a, x, start, end):
    if start > end:
        return -1

    mid = (start + end) //2
    if a[mid] == x:
        return mid
    elif a[mid] < x:
        return search(a,x,mid+1,end)
    else:
        return search(a,x,start,mid-1)

def sea(a,x):
    return search(a,x,0,len(a)-1)

d = [1,4,9,16,25,36,49,64,81]
print(sea(d,36))
print(sea(d,50))

