#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import queue
def bfs():
	global maze,N,M
	# print(maze)
	visit =[]
	q = queue.Queue()
	q.put((0,0,1,0))
	visit.append((0,0))
	while q.qsize() != 0:
		print(visit)
		_t = q.get()
		print(_t)

		if(_t[0] == N and _t[1] == M):
			print(_t[3])
			break

		if(_t[0] + 1 < N and maze[_t[0] + 1][_t[1]] != 'M' and (_t[0]+1, _t[1]) not in visit):
			print('1')
			if(maze[_t[0] + 1][_t[1]] == 'R'):
				q.put((_t[0] + 1, _t[1],_t[2],_t[3] + 1))
				visit.append((_t[0] + 1, _t[1]))
				
			if(maze[_t[0] + 1][_t[1]] == 'H' and _t[2] == 0):
				pass
				

			if(maze[_t[0] + 1][_t[1]] == 'H' and _t[2] == 1):
				print('aa')
				q.put((_t[0] + 1, _t[1],0,_t[3] + 1))
				visit.append((_t[0] + 1, _t[1]))
				



		if(_t[1] + 1 < M and maze[_t[0]][_t[1] + 1] != 'M' and (_t[0], _t[1] + 1) not in visit):
			print('2')
			if(maze[_t[0]][_t[1] + 1] == 'R'):
				q.put((_t[0], _t[1] + 1,_t[2],_t[3] + 1))
				visit.append((_t[0],_t[1] + 1))
				
			if(maze[_t[0]][_t[1] + 1] == 'H' and t[2] == 0):
				pass

			if(maze[_t[0]][_t[1] + 1] == 'H' and t[2] == 1):
				print('bb')
				q.put((_t[0], _t[1] + 1,0,_t[3] + 1))
				visit.append((_t[0],_t[1] + 1))
				


		#left
		if(maze[_t[0]][_t[1] - 1] != 'M' and _t[1] - 1 > 0 and (_t[0], _t[1] - 1) not in visit):
			print('3')
			if(maze[_t[0]][_t[1] - 1] == 'R'):
				q.put((_t[0], _t[1] - 1,_t[2],_t[3] + 1))
				visit.append((_t[0],_t[1] + 1))
				
			if(maze[_t[0]][_t[1] - 1] == 'H' and t[2] == 0):
				print('b')

				
			if(maze[_t[0]][_t[1] - 1] == 'H' and t[2] == 1):
				print('cc')
				q.put((_t[0], _t[1] - 1,0,_t[3] + 1))
				visit.append((_t[0],_t[1] + 1))
				

		#up
		if(_t[0] - 1 > 0 and maze[_t[0] - 1][_t[1]] != 1 and (_t[0] - 1, _t[1]) not in visit):
			print('4')
			if(maze[_t[0] - 1][_t[1]] == 'R'):
				q.put((_t[0] - 1, _t[1],_t[2],_t[3] + 1))
				visit.append((_t[0] - 1, _t[1]))
							
			if(maze[_t[0] - 1][_t[1]] == 'H' and _t[2] == 0):
				print('c')
				
			if(maze[_t[0] - 1][_t[1]] == 'H' and _t[2] == 1):
				print('dd')
				q.put((_t[0] - 1, _t[1],0,_t[3] + 1))
				visit.append((_t[0] - 1, _t[1]))
				


N = 0
M = 0


if __name__ == '__main__':
	line = sys.stdin.readline().strip().split(' ')
	N = int(line[0])
	M = int(line[1])
	maze = [[0]*M for i in range(N)]
	print(maze)
	for y in range(N):
		t = sys.stdin.readline()
		for x in range(M):
			maze[y][x] = t[x]
	# print(maze)
	bfs()