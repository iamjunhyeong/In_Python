#NO.11656 접미사 배열
import sys 
input = sys.stdin.readline

S = input().rstrip()
st = []
for i in range(len(S)):
    st.append(S[i:])

print('\n'.join(sorted(st)))


