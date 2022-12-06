from collections import deque

a = [10, 20, 30, 40, 50]
d = deque(a)
d.rotate(1)
print(d)
d.rotate(-1)
print(d)