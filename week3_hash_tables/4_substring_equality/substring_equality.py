# python3

import sys
import random

class Solver:
	def __init__(self, s):
		self.s = s
		self.m1 = 10**9 + 7
		self.m2 = 10**9 + 9
		self.x = random.randint(1, 10**9)
		self._precompute()

	def ask(self, a, b, l):
		return s[a:a+l] == s[b:b+l]

	def _precompute(self):
		self.h1 = [0] * (len(self.s) + 1)
		self.h2 = [0] * (len(self.s) + 1)
		for i in range(1, len(self.s) + 1):
			self.h1[i] = (self.x * self.h1[i - 1] + ord(self.s[i - 1])) % self.m1
			self.h2[i] = (self.x * self.h2[i - 1] + ord(self.s[i - 1])) % self.m2

	def ask_fast(self, a, b, l):
		h1al = (self.h1[a + l] - pow(self.x, l, self.m1) * self.h1[a]) % self.m1
		h2al = (self.h2[a + l] - pow(self.x, l, self.m2) * self.h2[a]) % self.m2
		h1bl = (self.h1[b + l] - pow(self.x, l, self.m1) * self.h1[b]) % self.m1
		h2bl = (self.h2[b + l] - pow(self.x, l, self.m2) * self.h2[b]) % self.m2
		return (h1al == h1bl) and (h2al == h2bl)

s = sys.stdin.readline()
q = int(sys.stdin.readline())
solver = Solver(s)
for i in range(q):
	a, b, l = map(int, sys.stdin.readline().split())
	print("Yes" if solver.ask_fast(a, b, l) else "No")
