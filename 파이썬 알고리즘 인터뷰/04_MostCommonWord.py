from collections import Counter

paragraph = "Bob hit a ball, the hit BALL flew far after it was hit"
banned = ["hit"]

words = ""
for i in paragraph:
    if i.isalpha() or i == " ":
        words += i

words = words.lower().split()
for i in words:
    if i == banned[0]:
        words.remove(i)
cnt = Counter(words)

print(max(cnt, key=cnt.get))
    