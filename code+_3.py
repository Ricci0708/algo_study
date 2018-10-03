# -*- coding: utf-8 -*-
# UTF-8 encoding when using korean
import queue

m, n = map(int,input().split(' '))
cnt = m * n


q = queue.Queue()

q.put((0,0,0))
visit = [(0,0)]
move = [(-2,1),(-1,2),(1,2),(2,1),(-2,-1),(-1,-2),(2,-1),(1,-2)]
depth = 0
while q.qsize() != 0:
	t = q.get()
	if depth < t[2]:
		depth = t[2]
	cnt -= 1
	for i in range(len(move)):
		if(t[0] + move[i][0] in range(m) and t[1] + move[i][1] in range(n) and (t[0] + move[i][0], t[1] + move[i][1]) not in visit):
			visit.append((t[0] + move[i][0], t[1] + move[i][1]))
			q.put((t[0] + move[i][0], t[1] + move[i][1], t[2] +1))

if(cnt == 0):
	print("T"+str(depth))
else:
	print("F"+str(depth))