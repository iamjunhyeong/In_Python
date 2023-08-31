from collections import deque
import sys
input = sys.stdin.readline

n = int(input())
cards = deque()
for i in range(1,n + 1):
    cards.append(i)

while len(cards) != 1:
    cards.popleft()
    m = cards.popleft()
    cards.append(m)
print(cards[0])