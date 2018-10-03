from itertools import product
import queue

width = 4
height = 4
chess = list(product(range(width), range(height)))

def route(start):
	# stack = []
	q = queue.Queue()
	visited = set()
	# stack.append(start)
	q.put(start)

	max_depth = 0
	while q.qsize() != 0:
		depth, start_pos = q.get()
		visited.add(start_pos)
		if max_depth < depth:
			max_depth = depth

		result_pos_set = set()
		for pos in [(2, -1), (2, 1), (1, 2), (1, -2), (-2, 1), (-2, -1), (-1, -2), (-1, 2)]:
			result_pos = (start_pos[0] + pos[0], start_pos[1] + pos[1])
			if result_pos in chess and result_pos not in visited:
				result_pos_set.add(result_pos)

		for s in result_pos_set:
			pair = (depth+1, s)
			# stack.append(pair)
			q.put(pair)

		if not result_pos_set:
			print(max_depth)

	return visited


result = route((0, chess[0]))
if set(result) == set(chess):
	print("T", end='')
else:
	print("F", end='')

print(result)