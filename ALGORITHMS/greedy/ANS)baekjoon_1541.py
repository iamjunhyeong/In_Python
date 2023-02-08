#NO.1541 잃어버리 괄호
n = input().split('-')
num = []
for i in n:
    cnt = 0
    s = i.split('+')
    for j in s:
        cnt += int(j)
    num.append(cnt)
a = num[0]
for i in range(1, len(num)):
    a -= num[i]
print(a)
