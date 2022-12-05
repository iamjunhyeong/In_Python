#NO.10799 쇠막대기 
import sys
input = sys.stdin.readline

li = input().rstrip()
st = []
result = 0
for i in range(len(li)):
    if li[i] == '(':
        st.append('(')
    else:
        if li[i-1] == '(':
            st.pop()
            result += len(st)
        else:
            st.pop()
            result += 1
print(result)
