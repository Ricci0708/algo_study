import sys
import queue

# import queue
tmp = sys.stdin.readline().split()

class Stack(object):

   def __init__(self):
      self.items = []

   def push(self, item):
      self.items.append(item)

   def pop(self):
       return self.items.pop()

   def peek(self):
       return self.items[-1]

   def isEmpty(self):
       return len(self.items) == 0

graph = {}
for _ in range(int(tmp[1])):
	edge_s = sys.stdin.readline().split()
	edge_s[0] = int(edge_s[0])
	edge_s[1] = int(edge_s[1])
	if edge_s[0] not in graph:
		graph[edge_s[0]] = []
	if edge_s[1] not in graph:
		graph[edge_s[1]] = []

	if edge_s[1] not in graph[edge_s[0]]:
		graph[edge_s[0]].append(edge_s[1])
	if edge_s[0] not in graph[edge_s[1]]:
		graph[edge_s[1]].append(edge_s[0])


def dfs(graph, start):
	s = Stack()
	s.push(start)
	visited = []


	while (not s.isEmpty()):
		_t = s.pop()
		if _t not in visited:
			visited.append(_t)
			inputTostack = list(set(graph[_t]) - set(visited))
			inputTostack.sort(reverse = True)
			# print(inputTostack)
			# inputTostack.reverse()
			for i in range(len(inputTostack)):
				s.push(inputTostack[i])
	return visited

def bfs(graph, start):
	visited = []
	q = queue.Queue()
	q.put(start)
	visited.append(start)
	while (q.qsize()):
		# print(visited)
		_t = q.get(0)
		# if _t in visited:
		# 	continue
		# visited.append(_t)

		inputTostack = list(set(graph[_t]) - set(visited))
		inputTostack.sort(reverse = False)
		# print(inputTostack)
		for i in range(len(inputTostack)):
			if inputTostack[i] not in visited:
				visited.append(inputTostack[i])
				q.put(inputTostack[i])
	return visited

path = dfs(graph,int(tmp[2]))
# print(path)
for p in path:
	print(p, end=' ')
print()
path = bfs(graph,int(tmp[2]))
for p in path:
	print(p, end=' ')
print()