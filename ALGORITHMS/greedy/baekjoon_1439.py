#NO.1439 뒤집기
n = input()
o = list(n.split('1'))
l = list(n.split('0'))
cnt1 = 0
cnt2 = 0
for i in o:
    if len(i) > 0:
        cnt1 += 1

for i in l:
    if len(i) > 0:
        cnt2 += 1
print(min(cnt1,cnt2))