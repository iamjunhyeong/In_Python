def search(a):
    qu = []
    st = []
    for i in a:
        if a.isalpha():
            qu.append(i.lower())
            st.append(i.lower())

    while qu:
        if qu.pop(0) != st.pop():
            return False

    return True

n = input()
print(search(n))