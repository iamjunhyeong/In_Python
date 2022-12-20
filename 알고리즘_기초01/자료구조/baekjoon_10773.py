#NO.10773 제로
n = int(input())
st = []
for _ in range(n):
    a = int(input())
    if a == 0:
        st.pop(-1)
    else:
        st.append(a)
print(sum(st))