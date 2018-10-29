import sys

n = int(sys.stdin.readline().rstrip())

fact = [1,1,2,6,24,120,720]

def factorial(n):
	# print(n)
	try:
		fact[n]
	except IndexError:
		fact.append((factorial(n-1) * n)%10000000007)
	finally:
		# print(fact)
		return fact[n]

def calulate(n):
	ans = 0
	for i in range( (n / 3) +1 ):
		three = i
		remain = n - (3 * three)
		total = i + remain
		# print (i)
		if three == 1:
			d = remain
		elif remain == 1:
			d = three
		elif three == 0 or remain == 0:
			d = 1
		if factorial(total) == 0:
			d = 0
		else:
			d = factorial(total) / factorial(three) / factorial(remain)

		ans += d
		ans %= 10000000007 
	return ans

i = 1
while(True):
	if i * 10 > n:
		break
	factorial(i * 10)
	i += 1
# print(fact)
print(calulate(n))
