#NO.11655 ROT13
import sys 
input = sys.stdin.readline

st = []
for i in input():
    if i.isupper():
        if ord(i) > 77:
            st.append(chr(65+(ord(i)-78)))
        else:
            st.append(chr(ord(i)+13))
    elif i.islower():
        if ord(i) > 109:
            st.append(chr(97+(ord(i)-110)))
        else:
            st.append(chr(ord(i)+13))
    else: st.append(i)


print(''.join(st))