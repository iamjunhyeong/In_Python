#NO.10102 개표
n = int(input())
a = 0
b = 0
s = ''
for i in range(n):
    s = list(str(input()))
for i in range(n):
    if s[i] == 'A':
        a += 1
    else: 
        b += 1
if a > b:
    print('A')
elif a < b:
    print('B')
else:
    print('Tie')