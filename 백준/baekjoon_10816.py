import sys
input = sys.stdin.readline

n = int(input())
n_cards = sorted(list(map(int, input().split())))
m = int(input())
m_cards = list(map(int, input().split()))
hash = {}

for i in n_cards:
    if i in hash:
        hash[i] += 1
    else:
        hash[i] = 1

for i in m_cards:
    if i in hash:
        print(hash[i], end=' ')
    else:
        print(0, end=' ')