import sys 
input = sys.stdin.readline

n, k = map(int,input().split())
li = list(map(int,input().split()))

dict = {}
for i in li:
    if i not in dict:
        dict[i] = 0
    dict[i] += 1

plug = []
cnt = 0
for i in range(k):
    dict[li[i]] -= 1
    if li[i] in plug:
        continue

    if len(plug) < n:
        plug.append(li[i])
    else:
        minn = dict[plug[0]]
        ind = 0
        for j in range(1, len(plug)):
            if dict[plug[j]] < minn:
                minn = dict[plug[j]]
                ind = j
        plug.pop(ind)
        plug.append(li[i])
        cnt += 1       
print(cnt)