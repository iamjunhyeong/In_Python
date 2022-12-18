# NO>11005 진법변환 2
import sys
input = sys.stdin.readline

system = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
N, B = map(int, input().split())
answer = str()

while N != 0:
    answer += system[N % B]
    N //= B

print(answer[::-1])