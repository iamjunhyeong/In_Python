#NO.5597 과제 안 내신 분..?
arr = []
for _ in range(28):
    arr.append(int(input()))

for i in range(1,31):
    if i not in arr:
        print(i)