#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys

def enalrge(m, magnification):
	result = [[0] * (len(m[0])*magnification) for i in range(len(m)*magnification)]
	# print(result)
	for i in range(len(result)):
		for j in range(len(result[0])):
			result[i][j] = m[int(i/magnification)][int(j/magnification)]
	return result

m = [[0]*30 for i in range(30)]

if __name__ == '__main__':
	width, height, rotation, magnification, shift_X, shift_y = map(int, sys.stdin.readline().split(" "))
	m_ = [[0]*width for i in range(height)]
	for i in range(height):
		split = sys.stdin.readline().strip().split(' ')
		for j in range(width):
			# pixel = int(split[i])
			m_[i][j] = split[j]
	# print(m_)
	for i in range(rotation % 4):
		m_ = list(zip(*m_[::-1]))
	# print(m_)
	if magnification > 1:
		m_ = enalrge(m_,magnification)
	# print(m_)

	x = int((20 - len(m_[0])) / 2)
	y = int((20 - len(m_)) / 2)

	x += shift_X
	y += shift_y

	for i in range(len(m_)):
		for j in range(len(m_[0])):
			if(i + x in range(20) and j + y in range(20)):
				m[i+x][j+y]  = m_[i][j]

	for i in range(20):
		for j in range(20):
			print(m[i][j], end='')
		print()



