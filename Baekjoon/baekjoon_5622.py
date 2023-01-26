#NO.5622 다이얼
alpha = input()
d = ["ABC"] + ["DEF"] + ["GHI"] + ["JKL"] + ["MNO"] + ["PQRS"] + ["TUV"] + ["WXYZ"]

cnt = 0
for i in alpha:
    for j in range(8):
        if i in d[j]:
            cnt += j + 3
print(cnt)
