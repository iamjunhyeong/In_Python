# No. 9093 단어 뒤집기
import sys

n = int(sys.stdin.readline())
words = []
for _ in range(n):
    rev = []
    words = sys.stdin.readline().split()
    for word in words:
        rev.append(word[::-1])
    print(' '.join(map(str,rev)))