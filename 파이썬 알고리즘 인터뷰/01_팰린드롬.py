n = input()
a = [n[i].lower() for i in range(len(n)) if n[i].isalpha()]
print(len(a))
for i in range(len(a)//2):
    print(a[i],a[len(a)-i-1])
    if a[i] != a[len(a)-1-i]: 
        print('false')
        break
else: print('true')

print(a)