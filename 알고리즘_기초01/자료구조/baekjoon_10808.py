# NO. 10808 알파벳 세기
import string
import sys
input = sys.stdin.readline

s = input().rstrip()
dic = {}
for i in string.ascii_lowercase:
    dic[i] = 0

for i in s:
    dic[i] += 1

for i in dic:
    print(dic[i], end=' ')

# 숏코딩
# alphabet = [0 for _ in range(26)]
# for s in input():
#     alphabet[ord(s) - ord("a")] += 1
# print(*alphabet)