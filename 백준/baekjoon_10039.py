li = []
for _ in range(5):
    score = int(input())
    if score < 40:
        li.append(40)
    else:
        li.append(score)

print(sum(li)//5)