import sys

if __name__ == '__main__':
	ipAddressStr = sys.stdin.readline().strip()
	l = len(ipAddressStr)
	# print(ipAddressStr[3:6])
	# print(ipAddressStr[6:9])
	# print(ipAddressStr[9:])
	ans = []
	for i in range(1,4):
		a = ipAddressStr[:i]
		l_ = l - len(a)
		if(l_ > 9 or l_ < 3 or int(a) > 255):
			continue
		else:
			# print(a)
			for j in range(1,4):
				l_ = l - len(a)
				b = ipAddressStr[i:i+j]
				l_ -= len(b)
				if(l_ > 6 or l_ < 2 or int(b) > 255):
					continue
				else:
					# print(b)
					for  k in range(1,4):
						l_ = l - len(a) - len(b)
						c = ipAddressStr[i+j:i+j+k]
						l_ = l_ - len(c)
						# print(l_)
						# print(c)
						if(l_ > 3 or l_ < 1 or int(c) > 255):
							continue
						else:
							d = ipAddressStr[i+j+k:]
							# print(d)
							if(int(d) > 255):
								continue
							else:
								ans.append((a,b,c,d))
	ans.sort()
	for i in range(len(ans)):
		print(ans[i][0] + '.' + ans[i][1] + '.' + ans[i][2] + '.' + ans[i][3])
