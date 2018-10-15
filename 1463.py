import sys

a = int(sys.stdin.readline())

# print(a)

large_num = int(10e6 + 1)

c = [-1] * large_num
b = [False] * large_num

c[1] = 0
b[1] = True

print(type(b[1]))
def make_one(a):
	print(a)
	if b[a]:
		return c[a]

	t1 = large_num
	t2 = large_num
	t3 = large_num

	if a % 3 == 0:
		if not b[int(a/3)]:
			make_one(int(a/3))
		t1 = c[int(a/3)]
	if a % 2 == 0:
		if not b[int(a/2)]:
			make_one(int(a/2))
		t2 = c[int(a/2)]
	if not b[a-1]:
		make_one(a-1)
	t3 = c[a-1]

	c[a] = min(t1,t2,t3) + 1
	b[a] = True

make_one(a)
# for i in range(a):
# 	print(c[a])
