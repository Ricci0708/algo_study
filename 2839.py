import sys

s = int(sys.stdin.readline())

l = [-1,-1,-1,1,-1,1,2,-1,2,3]

for i in range(len(l), s + 1):
	if l[i - 3] == -1:
		if l[i-5] == -1:
			l.append(-1)
		else:
			l.append(l[i-5] + 1)
	elif l[i - 5] == -1:
		l.append(l[i-3] + 1)
	else:
		if l[i-3] < l[i-5]:
			l.append(l[i-3] + 1)
		else:
			l.append(l[i-5] + 1)

# print(l)
print(l[s]) 
	