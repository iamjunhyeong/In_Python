import sys
input = sys.stdin.readline

n, m = map(int, input().split())
know_people = set(input().split()[1:])
parties = []

for i in range(m):
	parties.append(set(input().split()[1:]))

for _ in range(m):
	for party in parties:
		if party & know_people:
			know_people = know_people.union(party)

cnt = 0
for party in parties:
	if party & know_people:
		continue
	cnt += 1
print(cnt)