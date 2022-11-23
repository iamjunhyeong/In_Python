# No. 11729 하노이 탑 이동순서
def hanoi(n, first, end, sub,a):
    global cnt
    cnt += 1
    if n == 1:
        a += (first, end)
        # print(first, end)
        return
    
    hanoi(n-1,first, sub, end, a)
    a += (first, end)
    # print(first, end)
    hanoi(n-1,sub,end,first, a)

n = int(input())
cnt = 0
arr = []
hanoi(n,1,3,2,arr)
print(cnt)
for i in range(0,len(arr),2):
    print(arr[i], arr[i+1], sep=' ')
