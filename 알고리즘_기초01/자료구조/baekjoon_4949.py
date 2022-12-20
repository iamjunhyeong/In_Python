# NO.4949 균형잡힌세상
import sys
input = sys.stdin.readline

while True:
    a = input()
    if a[0] == '.': break

    st = []
    for i in a:
        if i == '(' or i == '[':
            st.append(i)
        elif i == ')':
            if not st or st[-1] == '[':
                break
            st.pop(-1)
        elif i == ']':
            if not st or st[-1] == '(':
                break
            st.pop(-1)

    if st or not i == '\n':
        print("no")
    else:
        print("yes")
