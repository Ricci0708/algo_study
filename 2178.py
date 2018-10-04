import sys
import queue

def bfs(t,g):
	global maze, _t
	# prev = {}

	visit = []
	q = queue.Queue()
	q.put((t[0],t[1]))
	maze[0][0] = 0
	while (q.qsize()):
		_t = q.get()
		visit.append((_t[0],_t[1]))
		if(_t[0] == g[0] and _t[1] == g[1]):
			break

		#down
		if(_t[0] + 1 <= g[0] and maze[_t[0] + 1][_t[1]] == 1 and (_t[0]+1, _t[1]) not in visit):
			# print(_t[0]+1, _t[1])
			maze[_t[0]+1][_t[1]] = maze[_t[0]][_t[1]] + 1
			q.put((_t[0] + 1, _t[1]))
			# prev[(_t[0] + 1, _t[1])] = (_t[0],_t[1])
			visit.append((_t[0] + 1))

		#right
		if(_t[1] + 1 <= g[1] and maze[_t[0]][_t[1] + 1] == 1  and (_t[0], _t[1] + 1) not in visit):
			q.put((_t[0], _t[1] + 1))
			maze[_t[0]][_t[1] + 1] = maze[_t[0]][_t[1]] + 1

			# prev[(_t[0], _t[1] + 1)] = (_t[0],_t[1])
			visit.append((_t[0], _t[1] + 1))

		#left
		if(_t[1] - 1 >= 0 and maze[_t[0]][_t[1] - 1] == 1  and (_t[0], _t[1] - 1) not in visit):
			q.put((_t[0], _t[1] - 1))
			maze[_t[0]][_t[1] - 1] = maze[_t[0]][_t[1]] + 1

			# prev[(_t[0], _t[1] - 1)] = (_t[0],_t[1])
			visit.append((_t[0], _t[1] - 1))

		#up
		if(_t[0] - 1 >= 0 and maze[_t[0] - 1][_t[1]] == 1 and (_t[0] - 1, _t[1]) not in visit):
			q.put((_t[0] - 1, _t[1]))
			maze[_t[0] - 1][_t[1]] = maze[_t[0]][_t[1]] + 1
			# prev[(_t[0] - 1, _t[1])] = (_t[0],_t[1])
			visit.append((_t[0] - 1, _t[1]))
	

tmp = sys.stdin.readline().split()
maze = []

for i in range(int(tmp[0])):
	maze.append([])
	edge_s = sys.stdin.readline()
	for j in range(int(tmp[1])):
		maze[i].append(edge_s[j])
	maze[i] = list(map(int, maze[i]))


start = (0,0)
target = (int(tmp[0]) - 1 ,int(tmp[1]) -1)


bfs(start,target)

print(maze[target[0]][target[1]] + 1)
