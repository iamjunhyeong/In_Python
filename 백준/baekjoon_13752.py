n = int(input())
li = []
for i in range(n):
    li.append(int(input()))

for i in li:
    for j in range(i):
        print("=",end='')
    print()