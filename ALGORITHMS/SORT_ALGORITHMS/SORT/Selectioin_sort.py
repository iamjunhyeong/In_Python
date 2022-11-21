def select(a,b,n):
    for _ in range(n):
        min = a[0]
        for i in a:
            if min > i: min = i
        b.append(min)
        a.remove(min)
    return b


list1 = [35,9,2,85,17]
list2 = []
print(select(list1,list2,len(list1)))
