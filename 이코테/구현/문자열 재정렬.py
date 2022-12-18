n = input()
num = 0
res = []

for i in n:
    if i.isalpha():
        res.append(i)
    else:
        num += int(i)

res.sort()
if not num == 0:
    res.append(str(num))

print(''.join(res))