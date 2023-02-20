#NO.25314 코딩은 체육과목 입니다
n = int(input())
llong = ['long']
intt = 'int'
for _ in range(n//4-1):
    llong.append('long')

print(*llong, intt, end=' ',)